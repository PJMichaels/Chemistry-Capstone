import argparse
import json
# from posixpath import split
from pathlib import Path

from prepare import prepare_datasets
from featurize_split import split_dfs


### get args - should be argparse eventually
overwrite = False ### TBD what the default should be

### import params
if __name__ == "__main__":
    ### ideally this function will be executed in process_pipeline.py
    with open(Path("params.json"), 'r') as f:
        params = json.load(f)

    ### Unpack params.json
    datasets = params["datasets"]
    random_seed = params["general"]['random_seed']
    split_style = params["general"]['split_style']
    validation_percent = params["general"]['validation_percent']
    feature_representation = params["general"]["feature_representation"]

    ### process prepare.py
    file_list = prepare_datasets(datasets, overwrite)

    ### process featurize_split df --- might be memory issues keeping all of these datasets in memory so should output file names again
    split_paths = split_dfs(file_list, split_style, validation_percent, random_seed, feature_representation, overwrite)

    ### process train.py files
    ### next step is the train file



### parse args to determine which datasets to prepare and models to train
### additional arg to skip steps that have already been done??? by checking if anticipated
### output already exists?

### prepare datasets (subset if args show)

### train models (based on subset) - hyperparam optimization if arg selected?

### output evaluation results and visualization

