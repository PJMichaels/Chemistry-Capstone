from pathlib import Path
import pandas as pd


### what params do we need to import???

def train_models(training_paths: list, models_dict: dict, random_seed: int, tune_models = False, overwrite = False) -> list:
    '''
    Trains models from the params file for each of the training datasets provided and
    outputs pickled model files
    
    Args:
        training_paths: (list) A list of paths to featurized training datasets
        model_dict: (dict) params.models dictionary from the params.json file. Includes models to train and hyperparameters parameters
        random_seed: (int) The random state argument for model training, which enables reproducibility.
        tune_models: (bool) Setting True for this parameter initiates a grid search for all models and will update best parameters section of params.json
        overwrite: (bool) If true existing files are overwritten/re-featurized-split

    Returns ? Some sort of association between datasets and pkl files for eval script
    '''

    print("\nInitiating dataset training step")

    output_list = [] ### may want to change this to be a dictionary or something else
    steps_skipped = False

    print(training_paths)