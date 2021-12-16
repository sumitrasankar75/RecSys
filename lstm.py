#model is from sigir competition and adapted for local results
#-no wandb or upload required
#-uses more sessions
#-optimized parameters (higher learning rate, higher patience, less epochs)
#-results plotted


import matplotlib.pyplot as plt
import os
import time
import json
import csv
from datetime import datetime
from dotenv import load_dotenv
import gensim
from random import choice, shuffle
from uploader import upload_submission

import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import wandb
from wandb.keras import WandbCallback


#load envs from env file
load_dotenv(verbose=True, dotenv_path='upload.env')


def read_sessions_from_training_file(training_file: str, K: int = None):
    user_sessions = []
    current_session_id = None
    current_session = []
    with open(training_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader):
            # if a max number of items is specified, just return at the K with what you have
            if K and idx >= K:
                break
            # row will contain: session_id_hash, product_action, product_sku_hash
            _session_id_hash = row['session_id_hash']
            # when a new session begins, store the old one and start again
            if current_session_id and current_session and _session_id_hash != current_session_id:
                user_sessions.append(current_session)
                # reset session
                current_session = []
            # We extract actions from session
            if row['product_action'] == '' and row['event_type'] ==  'pageview':
                current_session.append('view')

            elif row['product_action'] != '':
                current_session.append(row['product_action'])
            # update the current session id
            current_session_id = _session_id_hash

    # print how many sessions we have...
    print("# total sessions: {}".format(len(user_sessions)))
    # print first one to check
    print("First session is: {}".format(user_sessions[0]))

    return user_sessions


def session_indexed(s):
    """
    Converts a session (of actions) to indices and adds start/end tokens

    :param s: list of actions in a session (i.e 'add','detail', etc)
    :return:
    """
    action_to_idx = {'start': 0, 'end': 1, 'add': 2, 'remove': 3, 'purchase': 4, 'detail': 5, 'view': 6}
    return [action_to_idx['start']] + [action_to_idx[e] for e in s] + [action_to_idx['end']]


def prepare_training_data(sessions):
    """

    Convert extracted session into training data

    :param sessions: list of sessions
    :return:
    """

    purchase_sessions = []
    abandon_sessions = []
    for s in sessions:
        if 'purchase' in s and 'add' in s and s.index('purchase') > s.index('add'):
            first_purchase = s.index('purchase')
            p_session = s
            if s.count('purchase') > 1:
                second_purchase = s.index('purchase', first_purchase+1)
                p_session = s[:second_purchase]
            # remove actual purchase from list
            p_session.pop(first_purchase)
            purchase_sessions.append(p_session)
            assert not any( e == 'purchase' for e in p_session)

        elif 'add' in s and not 'purchase' in s:
            abandon_sessions.append(s)

    purchase_sessions = [session_indexed(s) for s in purchase_sessions]
    abandon_sessions = [session_indexed(s) for s in abandon_sessions]

    # combine session with purchase and abandon
    x = purchase_sessions + abandon_sessions

    # give label=1 for purchase, label=0 for abandon
    y = [1]*len(purchase_sessions) +[0]*len(abandon_sessions)
    assert len(x) == len(y)

    return x, y

def train_lstm_model(x, y,
                     epochs=200,
                     patience=18,
                     lstm_dim=48,
                     batch_size=128,
                     lr=1e-3):
    """
    Train an LSTM to predict purchase (1) or abandon (0)

    :param x: session sequences
    :param y: target labels
    :param epochs: num training epochs
    :param patience: early stopping patience
    :param lstm_dim: lstm units
    :param batch_size: batch size
    :param lr: learning rate
    :return:
    """


    X_train, X_test, y_train, y_test = train_test_split(x,y)
    # pad sequences
    max_len = max(len(_) for _ in x)
    X_train = pad_sequences(X_train, padding="post",value=7, maxlen=max_len)
    X_test = pad_sequences(X_test, padding="post", value=7, maxlen=max_len)

    # convert to one-hot
    X_train = tf.one_hot(X_train, depth=7)
    X_test = tf.one_hot(X_test, depth=7)

    y_train = np.array(y_train)
    y_test = np.array(y_test)

    # Define Model
    model = keras.Sequential()
    model.add(keras.layers.InputLayer(input_shape=(None,7)))
    model.add(keras.layers.Masking())
    model.add(keras.layers.LSTM(lstm_dim))
    model.add(keras.layers.Dense(1,activation='sigmoid'))
    model.summary()

    # Some Hyper Params
    opt = keras.optimizers.Adam(learning_rate=lr)
    loss = keras.losses.BinaryCrossentropy()
    es = keras.callbacks.EarlyStopping(monitor='val_loss',
                                       patience=patience,
                                       verbose=1,
                                       restore_best_weights=True)

    callbacks = [es]
    model.compile(optimizer=opt,
                  loss=loss,
                  metrics=['accuracy'])

    # Train Model
    history=model.fit(X_train,y_train,
              validation_data=(X_test,y_test),
              batch_size=batch_size,
              epochs=epochs,
              callbacks=callbacks)
    
    #plotting model
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='lower right')
    plt.show()

    plt.plot(history.history['loss'])  
    plt.plot(history.history['val_loss'])  
    plt.title('model loss')  
    plt.ylabel('loss')  
    plt.xlabel('epoch')  
    plt.legend(['train', 'test'], loc='upper right')  
    plt.show()
    
    # return trained model
    return model




def train_lstm(upload=False):
    print("Starting training at {}...\n".format(datetime.utcnow()))
    sessions = read_sessions_from_training_file(
        training_file='browsing_train.csv'
    )

    x, y = prepare_training_data(sessions)
    lstm_model = train_lstm_model(x,y)

    print("\nFinished at {}".format(datetime.utcnow()))

    return
    


if __name__ == "__main__":
    train_lstm(upload=False)