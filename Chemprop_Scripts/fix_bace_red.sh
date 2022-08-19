#!/bin/bash
echo bace


echo predicting_bace_validation_cluster_split
chemprop_predict \
    --test_path data_split_cleaned/bace-cluster-validate.csv \
    --preds_path Complex_Models/Predictions/bace-cluster-validate-pred.csv \
    --checkpoint_dir Complex_Models/bace-cluster \
    --smiles_columns mol \
    --features_generator morgan
    
    
echo predicting_bace_validation_random_split
chemprop_predict \
    --test_path data_split_cleaned/bace-random-validate.csv \
    --preds_path Complex_Models/Predictions/bace-random-validate-pred.csv \
    --checkpoint_dir Complex_Models/bace-random \
    --smiles_columns mol \
    --features_generator morgan



