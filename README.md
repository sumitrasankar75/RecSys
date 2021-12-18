# RecSys

This github features data and code for building a recomendation system. The inital dataset can be found on SIGIR eCom'21 website. 
 2 tasks were performed: Task 1 - Session - Based Recomendation & Task 2 - Purchase Prediction 
 
 Task 1 File Include: 
 
 Task 1 files can be found in the following folder
 
 /home/sumitra//recsys_folder/competitions/SIGIR_eCommerce_Challenge_2021/Rec_Sys
 
 The following is the container I created for the preprocessing notebook.
 
 docker run --name sumitra1 -it --gpus device=1 -p 8872:8872 --ipc=host -v /home/sumitra/recsys_folder/competitions/SIGIR_eCommerce_Challenge_2021:/recsys/    nvcr.io/nvidia/merlin/merlin-pytorch-training:0.6
 
 To run the preprocessing notebook: (preprocessing-Copy1-2.ipynb) 
 
 1. source /opt/conda/bin/activate
  
 2. conda activate recsys
 
 3. docker exec -it a10ece653fd3 bash
 
 4. cd /recsys

 5. jupyter-lab --allow-root --ip='0.0.0.0' --NotebookApp.token='' --port=8872
 
 6. Open in browser http://10.10.11.64:8872/

 7. Go to Rec_Sys folder to run the preprocessing notebook. (preprocessing-Copy1-2.ipynb)
 
 The following is the container I created for model training and evaluation.
 
 docker run --name sumitrasankarasub3 --gpus device=0 -it --ipc=host -p 8870:8870 -v /home/sumitra/recsys_folder/competitions/SIGIR_eCommerce_Challenge_2021:/recsys/ nvcr.io/nvidia/merlin/merlin-pytorch-training:21.11 /bin/bash
 
 To run model training and evaluation notebook: (gru_recsys.ipynb) 
 
 1. source /opt/conda/bin/activate
  
 2. conda activate recsys
 
 3. docker exec -it 43c783764608 bash
 
 4. cd /recsys

 5. jupyter-lab --allow-root --ip='0.0.0.0' --NotebookApp.token='' --port=8870
 
 6. Open in browser http://10.10.11.64:8870/

 7. Go to Rec_Sys folder to run the GRU model notebook. (gru_recsys.ipynb, xlnet_recsys.ipynb)
 
 The transformer model has some errors and needs to be fixed.
 
 Task_1_schema_features.pb - schema object (text file) - features to train the model
 
 Task_1_results.txt - A text file to save the GRU model results
 
 
 
 
 Task 2 Files Include:
 
 
 
 Feature engineer(1) - merging the three csvs ( browing_train, sku_train, search_train) and created additional and meaningful features
 
 Task 2 Models- the truncations of the data that created the task_2 csv used for the models & Random Forest, Gradient Boost, and XG Boost used for model prediction. 
 
 task_2 - sample data set of the first 9,999 rows. (original dataset contains 214,585 rows) 
