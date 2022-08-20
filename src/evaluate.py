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

### not sure how best to detail cluster vs random split, maybe these are two separate outputs

def get_chemprop_results():
    '''
    Function gets results from Complex Models folder if it exists... this is pretty dirty code that would be good to cleanup if/when time allows
    '''
    chemprop_predict_dir = Path.cwd() / "Complex_Models" / "Predictions"
    chemprop_results_path = Path.cwd() / "evaluation" / "Chemprop_Results.csv"

    if chemprop_predict_dir.exists():
        eval_results = {}

        datasets = ["bace", "clintox", "deepchem_Lipophilicity", "HIV", "sol_del", "tox21"]

        data_map={
            'HIV.csv': {'target':'HIV_active','structure':'smiles'},
            'bace.csv':{'target':'active','structure':'mol'},
            'tox21.csv':{'target':'NR-AhR','structure':'smiles'},
            'clintox.csv':{'target':'CT_TOX','structure':'smiles'},
            'sol_del.csv':{'target':'binned_sol','structure':'smiles'},
            'deepchem_Lipophilicity.csv':{'target':'drug_like','structure':'smiles'}   
        }

        pred_threshold = 0.5

        for path in chemprop_predict_dir.iterdir():
            target = [data_map[dataset]['target'] for dataset in data_map if dataset[:-4] in path.name][0]
            dataset = [dataset for dataset in data_map if dataset[:-4] in path.name][0]
            df = pd.read_csv(path)
            y_true = df["target_actual"].to_list()
            y_pred = df[target].apply(lambda x: 1 if x > pred_threshold else 0).to_list()
            y_pred_prob = df[target].to_list()

            eval_results[path.name] = {
                "dataset" : dataset,
                "accuracy_score": accuracy_score(y_true, y_pred),
                "balanced_accuracy_score": balanced_accuracy_score(y_true, y_pred),
                "f1_score": f1_score(y_true, y_pred),
                "roc_auc_score": roc_auc_score(y_true, y_pred_prob),
                "log_loss": log_loss(y_true, y_pred_prob),
                "matthews_corrcoef": matthews_corrcoef(y_true, y_pred)
            }
            
        df = pd.DataFrame(eval_results).T
        df = df.reset_index()
        df = df.rename(columns = {"index": "result_file"})
        df['split_id'] = df['result_file'].apply(lambda x: "train" if "train" in x else "validate")
        df['split_method'] = df['result_file'].apply(lambda x: "cluster" if "cluster" in x else "random")
        df['dataset'] = df['dataset'].apply(lambda x: "deepchem_lipophilicity.csv" if x == "deepchem_Lipophilicity.csv" else x)
        df['matthews_corrcoef']

        vis_df = df.melt(['result_file', 'dataset', 'split_id', 'split_method'], value_name = "score", var_name= "metric")

        vis_df['dataset'] = vis_df['dataset'].str[:-4]
        vis_df['dataset'] = vis_df['dataset'].str.replace('deepchem_', '')


        vis_df.sample(5)



        vis_df = vis_df[~ vis_df["result_file"].str.contains("hyperopt")]

        ### note that I needed to remove hyper-parameter optimizations results
        vis_df[(vis_df["dataset"] == 'bace') & (vis_df['split_method'] == "cluster")]

        ### write out dataframe to csv for later comparison with simple model results
        vis_df["model"] = 'Chemprop'
        print(f"Generating Chemprop evaluation metrics: {chemprop_results_path.relative_to(Path.cwd())}")
        vis_df.to_csv(chemprop_results_path, index = False)



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

    sklearn_predict_dir = Path.cwd() / "Simple_Models" / "Predictions"
    
    eval_output_path = Path.cwd() / "evaluation" / "Scikit-learn_Model_Results.csv"
    chemprop_results_path = Path.cwd() / "evaluation" / "Chemprop_Results.csv" ### will remove this if works
    combined_results_path = Path.cwd() / "evaluation" / "Combined_Results.csv"

    result_data = []

    for predictions_path in sklearn_predict_dir.iterdir():
        dataset, split_method, split_id, _ = tuple(predictions_path.name.split('-'))
        df = pd.read_csv(predictions_path)
        models = [x.replace("_pred_prob", "") for x in df.columns if "pred_prob" in x]

        for model in models:
            y_true = df['labels'].to_list()
            y_pred = df[f'{model}_pred'].to_list()
            y_pred_prob = df[f'{model}_pred_prob'].to_list()

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
    


    ### it would be good to replace this with my chemprop eval notebook code
    try:
        get_chemprop_results()
    except:
        "Unable to generate Chemprop results at this time."

    if chemprop_results_path.exists():
        chemprop_df = pd.read_csv(chemprop_results_path)
        chemprop_df.columns = [c.lower() for c in chemprop_df.columns]

        combined_df = pd.concat([result_df, chemprop_df])
        print(f"Generating combined Sklearn and Chemprop evaluation metrics: {eval_output_path.relative_to(Path.cwd())}")
        combined_df.to_csv(combined_results_path, index = False)
        

### Next step would be processing cross val results

