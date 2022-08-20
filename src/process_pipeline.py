import argparse
import json
from pathlib import Path

from prepare import prepare_datasets
from featurize_split import split_dfs
from train import train_models
from evaluate import evaluate_models

import warnings
warnings.filterwarnings("ignore")


parser = argparse.ArgumentParser(description='Get pipeline processing arguments')

parser.add_argument("--overwrite", "-o", action = "store_true", help= "Optional argument: If passed, this forces re-processing and overwrite of files that already exist")
parser.add_argument("--param_path", "-p", default= "params.json" , help= "Optional argument: Allows you to choose a custom params.json file path")
parser.add_argument("--eval_only", "-e", action= "store_true" , help= "Optional argument: If passed, this skips all steps but evaluation")

parsed_args = parser.parse_args()

overwrite = parsed_args.overwrite
eval_only = parsed_args.eval_only
param_path = Path.cwd() / parsed_args.param_path

if not param_path.exists():
    print(f"\nCould not find parameter file at provided path:\n{param_path}")
    exit()

with open(Path(param_path), 'r') as f:
    params = json.load(f)

### Unpack params.json
datasets = params["datasets"]
random_seed = params["general"]['random_seed']
split_style = params["general"]['split_style']
validation_percent = params["general"]['validation_percent']
feature_representation = params["general"]["feature_representation"]
models = params["models"]
metrics = params["evaluation_metrics"]

if not eval_only:
    ### process prepare.py
    file_list = prepare_datasets(datasets, overwrite)

    ### process featurize_split df --- might be memory issues keeping all of these datasets in memory so should output file names again
    split_paths = split_dfs(file_list, split_style, validation_percent, random_seed, feature_representation, overwrite)

    ### process train.py files
    training_paths = [train_path for train_path, _ in split_paths]
    train_models(training_paths, models, feature_representation, random_seed, overwrite)
else:
    print("--eval_only arg applied - skipping all steps but evaluation")

### process evaluation.py step
evaluate_models(metrics)
