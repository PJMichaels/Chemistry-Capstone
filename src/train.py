import yaml
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle


try:
    params = yaml.safe_load(open("params.yaml"))["train"]
    gen_params = yaml.safe_load(open("params.yaml"))["general"]
    max_iterations = params['max_iter']
    y_id = gen_params['y']
    random_seed = gen_params['seed']
    # mol_rep = params['mol_representation']
except:
    print('There is a problem during import of params.yaml for train.py')
    exit()

### from YAML import split params or maybe eventually cross val info as well as random state
### random state could also be hard coded maybe
### YAML PARAMS will also either need to note X and Y column names to know what labels are

train_path = Path.cwd() / "data" / "featurized" / "train.csv"
artifacts_dir = Path.cwd() / "pipeline_artifacts"
if not artifacts_dir.exists():
    artifacts_dir.mkdir()
model_path = artifacts_dir / "model.pkl"

train_df = pd.read_csv(train_path)

X_train = train_df.iloc[:,:-1]
y_train = list(train_df[y_id])



### will need to find a way to make model import into a variable as well and ensure
### there is a validation check that the model is spelled correctly, etc..
### how to import a variable?

### YAMLS params for the model? how to avoid making this too complicated
### one pipeline per model type, or one pipeline for all model types, but 
### params may be quite different for each model

### take a time stamp here so we can also note model train time if not captured elsewhere
print("\nBeggining to train model")
clf = LogisticRegression(random_state= random_seed ,solver='lbfgs',max_iter= max_iterations, verbose= True)
clf.fit(X_train, y_train)

print(f"\nWriting model to filepath:\n{model_path}")
pickle.dump(clf, open(model_path, 'wb'))

### take another time stamp and calculate/record delta for metrics
### pickle model here

### add some cmd line outputs for sanity!

