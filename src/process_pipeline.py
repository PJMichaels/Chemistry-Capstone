import argparse
import json
from pathlib import Path

from prepare import prepare_datasets
from featurize_split import split_dfs
from train import train_models
# from evaluate import eval_models


parser = argparse.ArgumentParser(description='Get pipeline processing arguments')

parser.add_argument("--overwrite", "-o", action = "store_true", help= "Optional argument: If passed, this forces re-processing and overwrite of files that already exist")
parser.add_argument("--param_path", "-p", default= "params.json" , help= "Optional argument: Allows you to choose a custom params.json file path")

parsed_args = parser.parse_args()

overwrite = parsed_args.overwrite
param_path = Path.cwd() / parsed_args.param_path

if not param_path.exists():
    print(f"\nCould not find parameter file at provided path:\n{param_path}")
    exit()

with open(Path("params.json"), 'r') as f:
    params = json.load(f)

### Unpack params.json
datasets = params["datasets"]
random_seed = params["general"]['random_seed']
split_style = params["general"]['split_style']
validation_percent = params["general"]['validation_percent']
feature_representation = params["general"]["feature_representation"]
models = params['models']

### process prepare.py
file_list = prepare_datasets(datasets, overwrite)

### process featurize_split df --- might be memory issues keeping all of these datasets in memory so should output file names again
split_paths = split_dfs(file_list, split_style, validation_percent, random_seed, feature_representation, overwrite)

### process train.py files
training_paths = [train_path for train_path, validate_path in split_paths]
model_paths = train_models(training_paths, models, feature_representation, random_seed, overwrite)

### process evaluation.py step
# eval_models(model_paths)

# ### get args - should be argparse eventually
# overwrite = False ### TBD what the default should be
# ### should add an optional arg to point to a different params.json file
# ### might eventually want a way to tune the models via command line

# ### import params
# if __name__ == "__main__":
#     ### ideally this function will be executed in process_pipeline.py
#     with open(Path("params.json"), 'r') as f:
#         params = json.load(f)

#     ### Unpack params.json
#     datasets = params["datasets"]
#     random_seed = params["general"]['random_seed']
#     split_style = params["general"]['split_style']
#     validation_percent = params["general"]['validation_percent']
#     feature_representation = params["general"]["feature_representation"]
#     models = params['models']

#     ### process prepare.py
#     file_list = prepare_datasets(datasets, overwrite)

#     ### process featurize_split df --- might be memory issues keeping all of these datasets in memory so should output file names again
#     split_paths = split_dfs(file_list, split_style, validation_percent, random_seed, feature_representation, overwrite)

#     ### process train.py files
#     training_paths = [train_path for train_path, validate_path in split_paths]
#     train_models(training_paths, models, feature_representation, random_seed, overwrite)
    
#     ### process evaluation.py step



# ### parse args to determine which datasets to prepare and models to train
# ### additional arg to skip steps that have already been done??? by checking if anticipated
# ### output already exists?

# ### prepare datasets (subset if args show)

# ### train models (based on subset) - hyperparam optimization if arg selected?

# ### output evaluation results and visualization

