from asyncore import write
from email.policy import default
from unittest import skip
import pandas as pd
# import seaborn as sns
# import os
from pathlib import Path
import json
from collections import defaultdict
# import math

def clean_dataset(dataset: str, dataset_dict: dict) -> pd.DataFrame:
    '''Takes a single dataset default dictionary cleans it, and writes a new .csv file'''
    dataset_path = Path.cwd() / "data" / (dataset + dataset_dict["suffix"])
    if not dataset_path.exists:
        print(f"Can't find {dataset_path}")
        return None
    
    df = pd.read_csv(dataset_path)


    


    return df


def prepare_datasets(datasets: dict, overwrite: bool = False) -> None:
    '''Takes in a dictionary of datasets, intended for the params[datasets] dictionary'''
    
    ### convert each dataset dict to defaultdict to simplify boolian logic
    datasets = {dataset: defaultdict(str,datasets[dataset]) for dataset in datasets}

    steps_skipped = False
    prepared_dir = Path.cwd() / "data" / "prepared"
    
    for dataset in datasets:

        output_path = prepared_dir / (dataset + ".csv")
        if datasets[dataset]["short_name"]:
            output_path = prepared_dir / (datasets[dataset]["short_name"] + ".csv")

        print(output_path)
        
        if not output_path.exists() or overwrite == True:
            
            with open(output_path, 'w') as f:
                df = clean_dataset(dataset, datasets[dataset])
                df.to_csv(output_path, index = False)
                print(f"Generated {output_path}")
        else:
            print(f"Dataset for {dataset} already exists:{output_path}\n")
            steps_skipped = True
    
    if steps_skipped:
        print("\nSkipped steps can be reprocessed by including --overwrite parameter")
    # x = 10
    # print(eval("x > 6"))




with open(Path("params.json"), 'r') as f:
    params = json.load(f)

prepare_datasets(params["datasets"], overwrite = True)

