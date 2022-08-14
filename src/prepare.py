import pandas as pd
from pathlib import Path
import json
from collections import defaultdict


def clean_dataset(dataset: str, dataset_dict: dict) -> pd.DataFrame:
    '''
    Takes a single dataset default dictionary, reads the associated file, and outputs a cleaned dataframe
    
    Args:
        dataset: (str) The name of the dataset being processed - needed to read file
        dataset_dict: (dict) The dictionary associated with the params.dataset containing preparation instructions

    Returns a pandas dataframe
    '''
    dataset_path = Path.cwd() / "data" / (dataset + dataset_dict["suffix"])
    if not dataset_path.exists:
        print(f"Can't find {dataset_path}")
        return None

    df = pd.read_csv(dataset_path)

    ### creating a set of columns to filter on for prepared df
    columns = []

    X_name = dataset_dict["X"]
    y_name = dataset_dict['y']

    ### standardizing X column name to reduce need for dataset params later on
    if X_name != "smiles":
        df['smiles'] = df[X_name]
    columns.append('smiles')

    ### enables binning of continuous data for classification with provided logic
    if dataset_dict['y_process']:
        logic = dataset_dict['y_process'].strip()
        df['labels'] = df[y_name].apply(lambda x: 1 if eval(logic) else 0)
    else:
        df['labels'] = df[y_name]
    
    columns.append("labels")
    
    ### persist a copy of labels column with identifiable name if provided - necessary for chemprop
    if dataset_dict['y_new']:
        y_new = dataset_dict["y_new"]
        df[f"labels-{y_new}"] = df['labels']
        columns.append(f"labels-{y_new}")
    else:
        df[f'labels-{y_name}'] = df['labels']
        columns.append(f"labels-{y_name}")

    
    ### filter df to only relevant columns for training and label-id copy column
    df = df[columns]

    return df


def prepare_datasets(datasets: dict, overwrite: bool = False) -> list:
    '''
    Takes in a dictionary of datasets, intended for the params[datasets] dictionary. This utilizes both the
    clean dataset and split df functions above. 
    
    Args:
        params: (dict) Unpacked params.json file contents
        overwrite: (bool) If true existing files are overwritten/re-prepared

    Returns a list of file paths for all files that would have been generated (included those that already existed)
    '''

    print("\nInitiating dataset preparation step")

    ### convert each dataset dict to defaultdict to simplify boolian logic
    datasets = {dataset: defaultdict(str,datasets[dataset]) for dataset in datasets}

    file_paths = []
    steps_skipped = False
    
    prepared_dir = Path.cwd() / "data" / "prepared"
    if not prepared_dir.exists():
        prepared_dir.mkdir()
        print(f"Making output directory: {prepared_dir}")
    
    for dataset in datasets:
        suffix = datasets[dataset]["suffix"]
        output_path = prepared_dir / (dataset + ".csv")

        ### if short_name parameter provided, name file after this
        if datasets[dataset]["short_name"]:
            output_path = prepared_dir / (datasets[dataset]["short_name"] + ".csv")

        
        ### only process files if they don't exist or overwrite arg is passed
        if not output_path.exists() or overwrite == True:
            df = clean_dataset(dataset, datasets[dataset])
            df.to_csv(output_path, index = False)
            print(f"Generated {output_path}")
            

        else:
            print(f"Dataset csv for {dataset} already exists")
            steps_skipped = True
        
        ### append list to be returned
        file_paths.append(str(output_path))
    
    ### output a reminder that you can use overwrite arg
    if steps_skipped:
        print("\nSkipped steps can be reprocessed by including --overwrite or -o parameter")

    return file_paths