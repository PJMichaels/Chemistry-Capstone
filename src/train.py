from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


### from YAML import split params or maybe eventually cross val info as well as random state
### random state could also be hard coded maybe
### YAML PARAMS will also either need to note X and Y column names to know what labels are

# split the data:
X=[generate_fingerprint(mol,2,1024) for mol in df['smiles']]
y=df['HIV_active'].to_list()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


### will need to find a way to make model import into a variable as well and ensure
### there is a validation check that the model is spelled correctly, etc..
### how to import a variable?

### YAMLS params for the model? how to avoid making this too complicated
### one pipeline per model type, or one pipeline for all model types, but 
### params may be quite different for each model

### take a time stamp here so we can also note model train time if not captured elsewhere

clf = LogisticRegression(random_state=0,solver='lbfgs',max_iter=1000)
clf.fit(X_train,y_train)

### take another time stamp and calculate/record delta for metrics
### pickle model here

### add some cmd line outputs for sanity!

