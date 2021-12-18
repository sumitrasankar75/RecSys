# RecSys

This github features data and code for building a recomendation system. The inital dataset can be found on SIGIR eCom'21 website. 
 2 tasks were performed: Task 1 - Session - Based Recomendation & Task 2 - Purchase Prediction 
 
 Task 1 File Include: 
 
 preprocessing - preprocessing search and browsing data and merging with product metadata
 
 docker run --name sumitrasankarasub3 --gpus device=0 -it --ipc=host -p 8870:8870 -v /home/sumitra/recsys_folder/competitions/SIGIR_eCommerce_Challenge_2021:/recsys/ nvcr.io/nvidia/merlin/merlin-pytorch-training:21.11 /bin/bash
 
 gru_recsys - GRU Model Training and Evaluation
 
 xlnet_recsys - Transformer Model Training and Evaluation (Have some errors. Needs to be fixed)
 
 schema_features - schema object (text file) necessary to train and evaluate the models
 
 results - A text file to save the GRU model results
 
 
 
 
 Task 2 Files Include:
 
 
 
 Feature engineer(1) - merging the three csvs ( browing_train, sku_train, search_train) and created additional and meaningful features
 
 Task 2 Models- the truncations of the data that created the task_2 csv used for the models & Random Forest, Gradient Boost, and XG Boost used for model prediction. 
 
 task_2 - sample data set of the first 9,999 rows. (original dataset contains 214,585 rows) 
