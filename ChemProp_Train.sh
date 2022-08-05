#!/bin/bash
echo training_chemprop
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/bace_train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/bace \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns active\
    --smiles_columns mol \
    --num_folds 5 \
    --split_sizes [0.8,0.2,0] \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/bace_validate.csv\
    --features_generator morgan

echo predicting_bace_training
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/bace_train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace_train_pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace \
    --smiles_columns mol \
    --features_generator morgan

echo predicting_bace_validation
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/bace_validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace_validate_pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace \
    --smiles_columns mol \
    --features_generator morgan