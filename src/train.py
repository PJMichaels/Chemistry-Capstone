from pathlib import Path
import pandas as pd
from datetime import datetime
import pickle

from utils.generate_morgan_fp import generate_fingerprint

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.dummy import DummyClassifier


### what params do we need to import???

def eval_model_json(model, args_dict):
    '''
    Converts model, represented as a string, and args represented as a dict into a string
    that then gets executed as code into a classifier object.
    
    Args:
        model: (str) The model name we want evaluated as code. Must match an imported model class exactly.
        model_dict: (dict) params.models.model dictionary from the params.json file. Includes model's args.

    Returns an sklearn classifier object
    '''
    arg_string = model + "("
    for arg in args_dict:
        arg_string += arg + "= "
        if type(args_dict[arg]) == str:
            arg_string += f'"{args_dict[arg]}", '
        else: ### will fail if someone enters a dict or list type as an arg
            arg_string += f'{args_dict[arg]}, '
    
    arg_string = arg_string[:-2] + ")"
    return eval(arg_string)



def train_models(training_paths: list, models_dict: dict, feature_representation: str, random_seed: int, overwrite = False) -> list:
    '''
    Trains models from the params file for each of the training datasets provided and
    outputs pickled model files
    
    Args:
        training_paths: (list) A list of paths to featurized training datasets
        model_dict: (dict) params.models dictionary from the params.json file. Includes models to train and hyperparameters parameters
        feature_representation: (str) A string representation of morgan fingerprint with radius and bits encoded and separated by - Ex. morganfingerprint-2-1024
        random_seed: (int) The random state argument for model training, which enables reproducibility.
        tune_models: (bool) Setting True for this parameter initiates a grid search for all models and will update best parameters section of params.json
        overwrite: (bool) If true existing files are overwritten/re-featurized-split

    Returns ? Some sort of association between datasets and pkl files for eval script
    '''

    print("\nInitiating dataset training step")

    output_list = [] ### may want to change this to be a dictionary or something else
    steps_skipped = False
    models_wo_random_state = ["KNeighborsClassifier"]


    if "morganfingerprint" in feature_representation:
        _, radius, bits = tuple(feature_representation.split("-"))

    models_dir = Path.cwd() / "models"
    if not models_dir.exists():
        models_dir.mkdir()
        print(f"Making output directory: {models_dir}")

    for train_path in training_paths:
        model_data_dir = models_dir / Path(train_path).name.replace(".csv", "")
        if not model_data_dir.exists():
            model_data_dir.mkdir()
            print(f"Making output directory: {model_data_dir}")

        df = pd.read_csv(train_path)
        ### convert fp dtype back to object
        df['fp'] = df['smiles'].apply(lambda x: generate_fingerprint(x,int(radius),int(bits)))

        X_train = df['fp'].to_list()
        y_train = df['labels'].to_list()

        for model in models_dict:
            model_path = model_data_dir / (model + ".pkl")

            if not model_path.exists() or overwrite == True:

                print(f"Generating model: {model_path}")
                            
                ### add random seed to model args
                if model not in models_wo_random_state:
                    models_dict[model].update({"random_state": random_seed})

                start_time = datetime.now()
                clf = eval_model_json(model, models_dict[model])
                clf.fit(X_train, y_train)

                end_time = datetime.now()

                clf.train_time = end_time - start_time
                print(f"Train time: {clf.train_time}")

                with open(model_path, "wb") as f:
                    pickle.dump(clf, f)

            else:
                print(f"Model file already exists: {model_path}")
                steps_skipped = True
