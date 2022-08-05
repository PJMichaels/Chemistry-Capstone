#!/bin/bash
echo training_chemprop

chemprop_train --data_path ~/Chemistry-Capstone/HIV-2.csv --dataset_type classification --save_dir Chemistry-~/Capstone/test_chemprop --epochs 50 --extra_metrics accuracy f1 binary_cross_entropy --metric auc --target_columns HIV_active --smiles_columns smiles --num_folds 5