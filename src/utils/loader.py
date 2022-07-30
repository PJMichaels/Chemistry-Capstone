import pandas as pd
from pathlib import Path
import pickle
import json


def load_featurized_train_test(y_id, test = True):
    '''
    Loads contents of featurized train and test data, and returns these in a ML ready format
    y_arg is the name of the label column, and should be a string.
    Optional arg test can be set to false to only return train data.
    '''

    train_df = pd.read_csv(Path.cwd() / "data" / "featurized" / "train.csv")
    X_train = train_df.iloc[:,:-1]
    y_train = list(train_df[y_id])

    if test:
        test_df = pd.read_csv(Path.cwd() / "data"/ "featurized" / "test.csv")
        X_test = test_df.iloc[:,:-1]
        y_test = list(test_df[y_id])
        return X_train, y_train, X_test, y_test
    
    return X_train, y_train 


def load_model(model_path = False):
    '''
    Loads in pickled model with one line.
    Optional arg model_path enables specification of where to read the pickled model from
    '''
    if not model_path:
        model_path = Path.cwd() / 'pipeline_artifacts' / 'model.pkl'
        
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    return model


def write_model(model, model_path = False):
    '''
    Loads in pickled model with one line.
    Optional arg model_path enables specification of where to read the pickled model from
    '''
    if not model_path:
        model_path = Path.cwd() / 'pipeline_artifacts' / 'model.pkl'

    if not model_path.parent.exists():
        model_path.parent.mkdir()

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

def write_scores(results_dict):
    scores_path = Path.cwd() / "scores.json"
    scores_string = json.dumps(results_dict, indent = 2)

    print("Model Eval Results:")
    print(scores_string)
    
    with open(scores_path, 'w') as f:
        f.write(scores_string)