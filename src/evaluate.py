from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.generate_morgan_fp import generate_fingerprint
import pickle

### it would be clever to make this a dynamic import, and maybe do the same with other scripts?
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import log_loss
from sklearn.metrics import matthews_corrcoef

# import altair as alt

### not sure how best to detail custer vs random split, maybe these are two separate outputs


def evaluate_models(model_paths: list, eval_metrics: dict, feature_representation: str, overwrite: bool = False):
    '''
    Assesses models based on paths to the pickled models and evaluation metrics passed to this function.
    
    Args:
        model_paths: (list) A list of paths to trained and pickled models
        eval_dict: (dict) params.eval_metrics dictionary from the params.json file. Includes the sklearn metrics to apply in output.
        feature_representation: (str) A string representation of morgan fingerprint with radius and bits encoded and separated by - Ex. morganfingerprint-2-1024
        overwrite: (bool) If true existing files are overwritten/re-featurized-split

    Returns ? Some sort of association between datasets and pkl files for eval script
    '''

    print("\nInitiating model evaluation step")

    ### iterate through model_paths and make a dictionary that has dataset, then a list of model_path objects
    ### I will then iterate through everything to do the eval.

    train_sets = {}
    data_dir = Path.cwd() / "data" / "split"

    if "morganfingerprint" in feature_representation:
        _, radius, bits = tuple(feature_representation.split("-"))

    result_data = []

    eval_dir = Path.cwd() / "evaluation"
    if not eval_dir.exists():
        eval_dir.mkdir()

    ### need to figure out if this is going to get overwritten, appended to, or get a unique name...
    eval_output_path = eval_dir / "Scikit-learn_Evaluation_Results.csv"

    if not eval_output_path.exists() or overwrite == True:

        for model_path in model_paths:
            path = Path(model_path)
            train_path = data_dir / (path.parent.name + ".csv")
            
            if train_path not in train_sets.keys():
                train_sets[train_path] = []
            
            train_sets[train_path].append(path)
            
        for train_path in train_sets:

            dataset = train_path.name.split("-")[0]
            split_method = train_path.name.split("-")[1]
            split_id = train_path.name.split("-")[1]

            train_df = pd.read_csv(train_path)
            train_df['fp'] = train_df['smiles'].apply(lambda x: generate_fingerprint(x,int(radius),int(bits)))
            X_train = train_df['fp'].to_list()
            y_train = train_df['labels'].to_list()

            validate_path = Path(str(train_path).replace("train", "validate"))
            validate_df = pd.read_csv(validate_path)
            validate_df['fp'] = validate_df['smiles'].apply(lambda x: generate_fingerprint(x,int(radius),int(bits)))
            X_validate = validate_df['fp'].to_list()
            y_validate = validate_df['labels'].to_list()

            for model_path in train_sets[train_path]:
                
                model = model_path.name.replace(".pkl", "")

                with open(model_path, 'rb') as f:
                    clf = pickle.load(f)
                
                y_train_pred = clf.predict(X_train)
                y_validate_pred = clf.predict(X_validate)

                for metric in eval_metrics:
                    metric_func = eval(metric)
                    ### train metric scores
                    score = metric_func(y_train, y_train_pred)
                    result_row = [dataset, split_method, "train", model, metric, score]
                    result_data.append(result_row)
                    ### validate metric scores
                    score = metric_func(y_validate, y_validate_pred)
                    result_row = [dataset, split_method, "validate", model, metric, score]
                    result_data.append(result_row)
                
                score = clf.train_time
                result_row = [dataset, split_method, "N/A", model, "fit_time", score]
                result_data.append(result_row)

        ### put all aggregated data into a dataframe
        result_df = pd.DataFrame(result_data, columns=["dataset", "split_method", "split_id", "model", "metric","score"])
        
        print(f"Gererating evaluation metrics: {eval_output_path.relative_to(Path.cwd())}")
        result_df.to_csv(eval_output_path, index= False)
        
    
    else:
        print(f"Evaluation results already exists: {eval_output_path.relative_to(Path.cwd())}")
        print("Skipped steps can be reprocessed by including --overwrite or -o parameter")