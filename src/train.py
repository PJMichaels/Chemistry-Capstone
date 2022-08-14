from pathlib import Path
import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.dummy import DummyClassifier


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
    models_dir = Path.cwd() / "models"

    if not models_dir.exists():
        models_dir.mkdir()
        print(f"Making output directory: {models_dir}")

    for train_path in training_paths:
        df = pd.read_csv(train_path)
        X_train = df['fp'].to_list()
        y_train = df['labels'].to_list()

        for model in models_dict:
            model_path = Path(train_path.replace(".csv", f"-{model}.pkl"))

            if not model_path.exists() or overwrite == True:
                ### this does not work and I need to solve this problem...
                clf = eval(model(models_dict[model]))
                clf.fit(X_train, y_train)

                with open(model_path, "wb") as f:
                    pickle.dump(clf, f)
                print(f"Generated model: {model_path}")

            else:
                print(f"Model file already exists: {model_path}")
                steps_skipped = True
