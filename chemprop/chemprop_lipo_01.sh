#!/bin/bash

chemprop_train \
--data_path ~/Chemistry-Capstone/data/deepchem_Lipophilicity.csv \
--dataset_type regression \
--save_dir ~/Chemistry-Capstone/chemprop/chemprep_lipo_01 \
--smiles_column smiles
--target_columns exp