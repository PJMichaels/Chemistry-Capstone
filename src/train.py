from pathlib import Path
import pandas as pd
from datetime import datetime
import pickle

from utils.generate_morgan_fp import generate_fingerprint

from sklearn.model_selection import cross_validate

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

    model_paths = []
    steps_skipped = False
    models_wo_random_state = ["KNeighborsClassifier"]
    cv_scoring = ['accuracy', 'f1','roc_auc','neg_log_loss']


    if "morganfingerprint" in feature_representation:
        _, radius, bits = tuple(feature_representation.split("-"))

    models_dir = Path.cwd() / "Simple_Models"
    if not models_dir.exists():
        models_dir.mkdir()
        print(f"Making output directory: {models_dir}")

    predictions_dir = models_dir / "Predictions"
    if not predictions_dir.exists():
        predictions_dir.mkdir()
        print(f"Making predictions output directory: {predictions_dir}")

    ### kind of an ugly solution, but this step eliminates featurization time if all models are trained
    required_training_paths = []
    for train_path in training_paths:
        model_data_dir = models_dir / Path(train_path).name.replace("-train.csv", "")
        for model in models_dict:
            model_path = model_data_dir / (model + ".pkl")

            if not model_path.exists() or overwrite == True:
                if train_path not in required_training_paths:    
                    required_training_paths.append(train_path)
            else:
                print(f"Model file already exists: {model_path.relative_to(Path.cwd())}")
                steps_skipped = True
                model_paths.append(str(model_path))


    for train_path in required_training_paths:
        model_data_dir = models_dir / Path(train_path).name.replace("-train.csv", "")
        if not model_data_dir.exists():
            model_data_dir.mkdir()
            print(f"Making output directory: {model_data_dir}")

        validate_path = Path(str(train_path).replace("train", "validate"))

        train_df = pd.read_csv(train_path)
        validate_df = pd.read_csv(validate_path)
        ### add fingerprint feature back to dataframe - unfortunately this is a duplicate effort right now
        train_df['fp'] = train_df['smiles'].apply(lambda x: generate_fingerprint(x,int(radius),int(bits)))
        validate_df['fp'] = validate_df['smiles'].apply(lambda x: generate_fingerprint(x,int(radius),int(bits)))

        X_train = train_df['fp'].to_list()
        y_train = train_df['labels'].to_list()
        X_validate = validate_df['fp'].to_list()
        y_validate = validate_df['labels'].to_list()

        for model in models_dict:
            model_path = model_data_dir / (model + ".pkl")

            if not model_path.exists() or overwrite == True:

                print(f"Generating model: {model_path}")
                            
                ### add random seed to model args
                if model not in models_wo_random_state:
                    models_dict[model].update({"random_state": random_seed})

                start_time = datetime.now()
                clf = eval_model_json(model, models_dict[model])

                cv_result=cross_validate(clf , X_train, y_train, scoring= cv_scoring, cv=5, return_estimator=False)
                pd.DataFrame(cv_result).describe().to_csv(str(model_path).replace('.pkl', '.csv'))

                clf.fit(X_train, y_train)

                end_time = datetime.now()

                ### make predictions and output predictions csv
                train_df[f"{model}_pred_prob"] = clf.predict_proba(X_train)[::,1]
                train_df[f"{model}_pred"] = clf.predict(X_train)

                validate_df[f"{model}_pred_prob"] = clf.predict_proba(X_validate)[::,1]
                validate_df[f"{model}_pred"] = clf.predict(X_validate)

                

                clf.train_time = end_time - start_time
                print(f"Train time: {clf.train_time}")

                with open(model_path, "wb") as f:
                    pickle.dump(clf, f)

            model_paths.append(str(model_path))
        
        ### write out prediction results to csv files in predictions directory
        train_df.drop(columns = "fp", inplace= True)
        train_pred_output = predictions_dir / (Path(train_path).name.replace(".csv", "-pred.csv"))
        train_df.to_csv(train_pred_output)

        validate_df.drop(columns = "fp", inplace= True)
        validate_pred_output = predictions_dir / (Path(validate_path).name.replace(".csv", "-pred.csv"))
        validate_df.to_csv(validate_pred_output)
        
    
    ### output a reminder that you can use overwrite arg
    if steps_skipped:
        print("\nSkipped steps can be reprocessed by including --overwrite or -o parameter")

    
    return model_paths