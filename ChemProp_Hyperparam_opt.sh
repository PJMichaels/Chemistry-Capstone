#!/bin/bash
echo bace
chemprop_hyperopt \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/bace-cluster-train.csv \
    --dataset_type classification \
    --num_iters 40 \
    --config_save_path ~/Chemistry-Capstone/Complex_Models/bace-cluster-hyperopt/hyper_param.json\
    --num_workers 1 \
    --smiles_columns mol \
    --target_columns active\
    
echo training_chemprop_bace_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/bace-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster-hyperopt \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns active\
    --smiles_columns mol \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/bace-cluster-validate.csv\
    --features_generator morgan \
    --num_workers 1 \
    --config_path ~/Chemistry-Capstone/Complex_Models/bace-cluster-hyperopt/hyper_param.json\

echo predicting_bace_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/bace-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-cluster-train-pred-hyperopt.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster-hyperopt \
    --smiles_columns mol \
    --num_workers 1 \
    --features_generator morgan

echo predicting_bace_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/bace-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-cluster-validate-pred-hyperopt.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster-hyperopt \
    --smiles_columns mol \
    --num_workers 1 \
    --features_generator morgan
    
