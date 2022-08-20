from pathlib import Path
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

from utils.generate_morgan_fp import generate_fingerprint
import pickle

### it would be clever to make this a dynamic import, and maybe do the same with other scripts?
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import log_loss
from sklearn.metrics import matthews_corrcoef

# import altair as alt

### not sure how best to detail custer vs random split, maybe these are two separate outputs


def evaluate_models(eval_metrics: dict, feature_representation: str, overwrite: bool = False):
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

    probability_based_metrics = ["log_loss", "roc_auc_score"]

    predict_dir = Path.cwd() / "Simple_Models" / "Predictions"
    eval_output_path = Path.cwd() / "evaluation" / "Scikit-learn_Model_Results.csv"
    chemprop_results_path = Path.cwd() / "evaluation" / "Chemprop_Results.csv"
    combined_results_path = Path.cwd() / "evaluation" / "Combined_Results"

    result_data = []

    for predictions_path in predict_dir.iterdir():
        dataset, split_method, split_id, _ = tuple(predictions_path.name.split('-'))
        df = pd.read_csv(predictions_path)
        models = [x.replace("_pred_prob", "") for x in df.columns if "pred_prob" in x]

        for model in models:
            y_true = df['labels']
            y_pred = df[f'{model}_pred']
            y_pred_prob = df[f'{model}_pred_prob']

            for metric in eval_metrics:
                metric_func = eval(metric)

                if metric in probability_based_metrics:
                    score = metric_func(y_true, y_pred_prob)
                else:
                    score = metric_func(y_true, y_pred)

                result_row = [predictions_path.name, dataset, split_id, split_method, metric, score, model]
                result_data.append(result_row)

    ### put all aggregated data into a dataframe
    result_df = pd.DataFrame(result_data, columns=["result_file" ,"dataset", "split_id", "split_method", "metric","score", "model"])
    
    print(f"Generating Sklearn evaluation metrics: {eval_output_path.relative_to(Path.cwd())}")
    result_df.to_csv(eval_output_path, index= False)
    
    if chemprop_results_path.exists():
        chemprop_df = pd.read_csv(chemprop_results_path)
        chemprop_df.columns = [c.lower() for c in chemprop_df.columns]

        combined_df = pd.concat([result_df, chemprop_df])
        print(f"Generating combined Sklearn and Chemprop evaluation metrics: {eval_output_path.relative_to(Path.cwd())}")
        combined_df.to_csv(combined_results_path, index = False)



### Next step would be processing cross val results


