#!/bin/bash
echo bace


echo interpreting_chemprop_Bace

chemprop_interpret \
    --data_path ~/Chemistry-Capstone/Chemprop_Interpret/cluster_4.csv\
    --checkpoint_dir ~/Chemistry-Capstone/Complex_Models/bace-cluster-hyperopt \
    --property_id 1 \
    --num_workers 1 \
    --smiles_columns smiles\
    --features_generator morgan\


