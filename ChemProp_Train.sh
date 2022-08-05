#!/bin/bash
echo bace

echo training_chemprop_bace_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/bace-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/bace-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns active\
    --smiles_columns mol \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/bace-random-validate.csv\
    --features_generator morgan

echo predicting_bace_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/bace-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-random \
    --smiles_columns mol \
    --features_generator morgan

echo predicting_bace_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/bace-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-random \
    --smiles_columns mol \
    --features_generator morgan

echo training_chemprop_bace_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/bace-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns active\
    --smiles_columns mol \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/bace-cluster-validate.csv\
    --features_generator morgan

echo predicting_bace_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/bace-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster \
    --smiles_columns mol \
    --features_generator morgan

echo predicting_bace_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/bace-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/bace-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster \
    --smiles_columns mol \
    --features_generator morgan
    
echo clintox

echo training_chemprop_clintox_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/clintox-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/clintox-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns CT_TOX\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/clintox-random-validate.csv\
    --features_generator morgan

echo predicting_clintox_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/clintox-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/clintox-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/clintox-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_clintox_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/clintox-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/clintox-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/clintox-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_clintox_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/clintox-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/clintox-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns CT_TOX\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/clintox-cluster-validate.csv\
    --features_generator morgan

echo predicting_clintox_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/clintox-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/clintox-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/clintox-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_clintox_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/clintox-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/clintox-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/clintox-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo Lipophilicity

echo training_chemprop_deepchem_Lipophilicity_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/deepchem_Lipophilicity-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/deepchem_Lipophilicity-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns drug_like\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/deepchem_Lipophilicity-random-validate.csv\
    --features_generator morgan

echo predicting_deepchem_Lipophilicity_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/deepchem_Lipophilicity-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/deepchem_Lipophilicity-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/deepchem_Lipophilicity-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_deepchem_Lipophilicity_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/deepchem_Lipophilicity-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/deepchem_Lipophilicity-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/deepchem_Lipophilicity-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_deepchem_Lipophilicity_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/deepchem_Lipophilicity-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/deepchem_Lipophilicity-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns drug_like\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/deepchem_Lipophilicity-cluster-validate.csv\
    --features_generator morgan

echo predicting_deepchem_Lipophilicity_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/deepchem_Lipophilicity-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/deepchem_Lipophilicity-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/deepchem_Lipophilicity-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_deepchem_Lipophilicity_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/deepchem_Lipophilicity-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/deepchem_Lipophilicity-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/deepchem_Lipophilicity-cluster \
    --smiles_columns smiles \
    --features_generator morgan
    
echo HIV

echo training_chemprop_HIV_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/HIV-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/HIV-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns HIV_active\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/HIV-random-validate.csv\
    --features_generator morgan

echo predicting_HIV_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/HIV-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/HIV-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/HIV-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_HIV_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/HIV-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/HIV-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/HIV-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_HIV_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/HIV-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/HIV-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns HIV_active\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/HIV-cluster-validate.csv\
    --features_generator morgan

echo predicting_HIV_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/HIV-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/HIV-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/HIV-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_HIV_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/HIV-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/HIV-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/HIV-cluster \
    --smiles_columns smiles \
    --features_generator morgan
    
echo solubility

echo training_chemprop_sol_del_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/sol_del-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/sol_del-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns binned_sol\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/sol_del-random-validate.csv\
    --features_generator morgan

echo predicting_sol_del_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/sol_del-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/sol_del-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/sol_del-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_sol_del_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/sol_del-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/sol_del-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/sol_del-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_sol_del_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/sol_del-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/sol_del-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns binned_sol\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/sol_del-cluster-validate.csv\
    --features_generator morgan

echo predicting_sol_del_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/sol_del-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/sol_del-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/sol_del-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_sol_del_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/sol_del-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/sol_del-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/sol_del-cluster \
    --smiles_columns smiles \
    --features_generator morgan
    
echo tox21

echo training_chemprop_tox21_random_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/tox21-random-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/tox21-random \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns NR-AhR\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/tox21-random-validate.csv\
    --features_generator morgan

echo predicting_tox21_training_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/tox21-random-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/tox21-random-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/tox21-random \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_tox21_validation_random_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/tox21-random-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/tox21-random-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/tox21-random \
    --smiles_columns smiles \
    --features_generator morgan

echo training_chemprop_tox21_cluster_split
chemprop_train \
    --data_path ~/Chemistry-Capstone/data_split_cleaned/tox21-cluster-train.csv \
    --dataset_type classification \
    --save_dir ~/Chemistry-Capstone/Complex_Models/tox21-cluster \
    --epochs 50 \
    --extra_metrics accuracy f1 binary_cross_entropy \
    --metric auc \
    --target_columns NR-AhR\
    --smiles_columns smiles \
    --num_folds 5 \
    --split_sizes 0.8 0 0.2 \
    --separate_val_path ~/Chemistry-Capstone/data_split_cleaned/tox21-cluster-validate.csv\
    --features_generator morgan

echo predicting_tox21_training_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/tox21-cluster-train.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/tox21-cluster-train-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/tox21-cluster \
    --smiles_columns smiles \
    --features_generator morgan

echo predicting_tox21_validation_cluster_split
chemprop_predict \
    --test_path ~/Chemistry-Capstone/data_split_cleaned/tox21-cluster-validate.csv \
    --preds_path ~/Chemistry-Capstone/Complex_Models/Predictions/tox21-cluster-validate-pred.csv \
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/tox21-cluster \
    --smiles_columns smiles \
    --features_generator morgan