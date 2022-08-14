import pandas as pd
import os

### it would be clever to make this a dynamic import, and maybe do the same with other scripts?
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import log_loss
from sklearn.metrics import matthews_corrcoef

# import altair as alt

### not sure how best to detail custer vs random split, maybe these are two separate outputs

def evaluate_models(model_paths: list, eval_dict: dict, overwrite: bool = False):
    '''
    Assesses models based on paths to the pickled models and evaluation metrics passed to this function.
    
    Args:
        model_paths: (list) A list of paths to trained and pickled models
        eval_dict: (dict) params.eval_metrics dictionary from the params.json file. Includes the sklearn metrics to apply in output.
        ? feature_representation: (str) A string representation of morgan fingerprint with radius and bits encoded and separated by - Ex. morganfingerprint-2-1024
        ? overwrite: (bool) If true existing files are overwritten/re-featurized-split

    Returns ? Some sort of association between datasets and pkl files for eval script
    '''

    print("\nInitiating model evaluation step")
    print(model_paths)