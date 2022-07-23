### does importing a pkl file require additional imports to use predict code???
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score


### import clf from .pkl artifact file

### this starts to get into the eval stage so should be removed eventually
y_train_pred=clf.predict(X_train)
y_test_pred=clf.predict(X_test)



# Score the model
result={}

result.update({'train':{'accuracy':accuracy_score(y_train, y_train_pred),
                       'f1':f1_score(y_train, y_train_pred)}})

result.update({'test':{'accuracy':accuracy_score(y_test, y_test_pred),
                       'f1':f1_score(y_test, y_test_pred)}})


### either output these metrics to csv results, or figure out how to get them
### tracked by dvc

### decide if we do or don't want to track these via command-line
print('Logistic Regression Result')
result # this isn't needed here, but left as a reminder to do something different

### not sure where exactly to do the dummy classifier script, but I'll put this
### here for now... maybe integrate this through the whole process as well??

from sklearn.dummy import DummyClassifier
dummy_clf = DummyClassifier(strategy="most_frequent")
dummy_clf.fit(X_train, y_train)
y_train_pred=dummy_clf.predict(X_train)
y_test_pred=dummy_clf.predict(X_test)

result_dummy={}
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

result_dummy.update({'train':{'accuracy':accuracy_score(y_train, y_train_pred),
                       'f1':f1_score(y_train, y_train_pred)}})

result_dummy.update({'test':{'accuracy':accuracy_score(y_test, y_test_pred),
                       'f1':f1_score(y_test, y_test_pred)}})
print('Dummy Result')
result_dummy