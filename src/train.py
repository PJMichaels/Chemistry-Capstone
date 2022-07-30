import yaml
import time
from sklearn.linear_model import LogisticRegression
from utils import loader


try:
    params = yaml.safe_load(open("params.yaml"))["train"]
    gen_params = yaml.safe_load(open("params.yaml"))["general"]
    max_iterations = params['max_iter']
    y_id = gen_params['y']
    random_seed = gen_params['seed']
except:
    print('There is a problem during import of params.yaml for train.py')
    exit()

### from YAML import split params or maybe eventually cross val info as well as random state
### random state could also be hard coded maybe
### YAML PARAMS will also either need to note X and Y column names to know what labels are

X_train, y_train = loader.load_featurized_train_test(y_id, test = False)


### will need to find a way to make model import into a variable as well and ensure
### there is a validation check that the model is spelled correctly, etc..
### how to import a variable?

### YAMLS params for the model? how to avoid making this too complicated
### one pipeline per model type, or one pipeline for all model types, but 
### params may be quite different for each model

### take a time stamp here so we can also note model train time if not captured elsewhere
print("\nBeggining to train model")
start_time = time.time()

clf = LogisticRegression(random_state= random_seed ,solver='lbfgs',max_iter= max_iterations, verbose= True)
clf.fit(X_train, y_train)

stop_time = time.time()

clf.train_time = f"{stop_time - start_time} seconds"

loader.write_model(clf)

### take another time stamp and calculate/record delta time for metrics

