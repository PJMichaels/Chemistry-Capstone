#!/bin/bash
echo bace

echo training_chemprop_bace_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/bace-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/bace-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    -- labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/bace-random-validate.csv\
    --features_generator morgan

echo predicting_bace_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/bace-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_bace_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/bace-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_bace_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/bace-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/bace-cluster-validate.csv\
    --features_generator morgan

echo predicting_bace_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/bace-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_bace_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/bace-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster \
    --smiles_columns smiles \
    --features_generator morgan
    
echo clintox

echo training_chemprop_clintox_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/clintox-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/clintox-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/clintox-random-validate.csv\
    --features_generator morgan

echo predicting_clintox_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/clintox-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/clintox-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/clintox-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_clintox_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/clintox-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/clintox-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/clintox-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_clintox_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/clintox-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/clintox-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/clintox-cluster-validate.csv\
    --features_generator morgan

echo predicting_clintox_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/clintox-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/clintox-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/clintox-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_clintox_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/clintox-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/clintox-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/clintox-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo lipophilicity

echo training_chemprop_lipophilicity_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/lipophilicity-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/lipophilicity-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/lipophilicity-random-validate.csv\
    --features_generator morgan

echo predicting_lipophilicity_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/lipophilicity-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/lipophilicity-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/lipophilicity-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_lipophilicity_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/lipophilicity-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/lipophilicity-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/lipophilicity-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_lipophilicity_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/lipophilicity-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/lipophilicity-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/lipophilicity-cluster-validate.csv\
    --features_generator morgan

echo predicting_lipophilicity_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/lipophilicity-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/lipophilicity-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/lipophilicity-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_lipophilicity_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/lipophilicity-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/lipophilicity-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/lipophilicity-cluster \
    --smiles_columns smiles \
    --features_generator morgan
    
echo HIV

echo training_chemprop_HIV_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/HIV-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/HIV-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/HIV-random-validate.csv\
    --features_generator morgan

echo predicting_HIV_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/HIV-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/HIV-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/HIV-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_HIV_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/HIV-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/HIV-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/HIV-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_HIV_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/HIV-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/HIV-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/HIV-cluster-validate.csv\
    --features_generator morgan

echo predicting_HIV_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/HIV-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/HIV-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/HIV-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_HIV_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/HIV-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/HIV-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/HIV-cluster \
    --smiles_columns smiles \
    --features_generator morgan
    
echo solubility

echo training_chemprop_sol_del_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/sol_del-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/sol_del-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/sol_del-random-validate.csv\
    --features_generator morgan

echo predicting_sol_del_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/sol_del-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/sol_del-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/sol_del-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_sol_del_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/sol_del-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/sol_del-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/sol_del-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_sol_del_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/sol_del-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/sol_del-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/sol_del-cluster-validate.csv\
    --features_generator morgan

echo predicting_sol_del_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/sol_del-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/sol_del-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/sol_del-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_sol_del_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/sol_del-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/sol_del-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/sol_del-cluster \
    --smiles_columns smiles \
    --features_generator morgan
    
echo tox21

echo training_chemprop_tox21_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/tox21-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/tox21-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/tox21-random-validate.csv\
    --features_generator morgan

echo predicting_tox21_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/tox21-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/tox21-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/tox21-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_tox21_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/tox21-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/tox21-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/tox21-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_tox21_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data/split/tox21-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/tox21-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns labels\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data/split/tox21-cluster-validate.csv\
    --features_generator morgan

echo predicting_tox21_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/tox21-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/tox21-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/tox21-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_tox21_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data/split/tox21-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/tox21-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/tox21-cluster \
    --smiles_columns smiles \
    --features_generator morgan
