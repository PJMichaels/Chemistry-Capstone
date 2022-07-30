import yaml
import json
from utils import loader
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
# from dvclive import Live # might need to do something for dvc to better track/compare results

try:
    # params = yaml.safe_load(open("params.yaml"))["evaluation"]
    gen_params = yaml.safe_load(open("params.yaml"))["general"]
    y_id = gen_params['y']
except:
    print('There is a problem during import of params.yaml for train.py')
    exit()

### import clf from .pkl artifact file
clf = loader.load_model()

X_train, y_train, X_test, y_test = loader.load_featurized_train_test(y_id)

### this starts to get into the eval stage
y_train_pred=clf.predict(X_train)
y_test_pred=clf.predict(X_test)


# Score the model
result={}
result['Model_Train_Time'] = clf.train_time
result['Accuracy Score - train'] = accuracy_score(y_train, y_train_pred)
result["F1 Score - train"] = f1_score(y_train, y_train_pred)
result['Accuracy Score - test'] = accuracy_score(y_test, y_test_pred)
result["F1 Score - test"] = f1_score(y_test, y_test_pred)


# result[.update({'train':{']accuracy':accuracy_score(y_train, y_train_pred),
#                        'f1':f1_score(y_train, y_train_pred)}})

# result.update({'test':{'accuracy':accuracy_score(y_test, y_test_pred),
#                        'f1':f1_score(y_test, y_test_pred)}})

print('Logistic Regression Result')

loader.write_scores(result)

### either output these metrics to csv results, or figure out how to get them
### tracked by dvc

### decide if we do or don't want to track these via command-line

### not sure where exactly to do the dummy classifier script, but I'll put this
### here for now... maybe integrate this through the whole process as well??



#### everything below here is probably trash code except dummy model which I need to also implement somehow


# from sklearn.dummy import DummyClassifier
# dummy_clf = DummyClassifier(strategy="most_frequent")
# dummy_clf.fit(X_train, y_train)
# y_train_pred=dummy_clf.predict(X_train)
# y_test_pred=dummy_clf.predict(X_test)

# result_dummy={}
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import f1_score

# result_dummy.update({'train':{'accuracy':accuracy_score(y_train, y_train_pred),
#                        'f1':f1_score(y_train, y_train_pred)}})

# result_dummy.update({'test':{'accuracy':accuracy_score(y_test, y_test_pred),
#                        'f1':f1_score(y_test, y_test_pred)}})
# print('Dummy Result')
# result_dummy




# import json
# import math
# import os
# import pickle
# import sys

# import pandas as pd
# from sklearn import metrics
# from sklearn import tree
# from dvclive import Live
# from matplotlib import pyplot as plt


# if len(sys.argv) != 3:
#     sys.stderr.write("Arguments error. Usage:\n")
#     sys.stderr.write("\tpython evaluate.py model features\n")
#     sys.exit(1)

# model_file = sys.argv[1]
# train_file = os.path.join(sys.argv[2], "train.pkl")
# test_file = os.path.join(sys.argv[2], "test.pkl")

# def evaluate(model, matrix, dataset_name):
#     """Dump all evaluation metrics and plots for given datasets."""
#     eval_path = os.path.join("evaluation", dataset_name)

#     labels = matrix[:, 1].toarray().astype(int)
#     x = matrix[:, 2:]

#     predictions_by_class = model.predict_proba(x)
#     predictions = predictions_by_class[:, 1]

#     # Use dvclive to log a few simple plots ...
#     live = Live(eval_path)
#     live.log_plot("roc", labels, predictions)
#     live.log("avg_prec", metrics.average_precision_score(labels, predictions))
#     live.log("roc_auc", metrics.roc_auc_score(labels, predictions))

#     # ... but actually it can be done with dumping data points into a file:
#     # ROC has a drop_intermediate arg that reduces the number of points.
#     # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve.
#     # PRC lacks this arg, so we manually reduce to 1000 points as a rough estimate.
#     precision, recall, prc_thresholds = metrics.precision_recall_curve(labels, predictions)
#     nth_point = math.ceil(len(prc_thresholds) / 1000)
#     prc_points = list(zip(precision, recall, prc_thresholds))[::nth_point]
#     prc_file = os.path.join(eval_path, "plots", "precision_recall.json")
#     with open(prc_file, "w") as fd:
#         json.dump(
#             {
#                 "prc": [
#                     {"precision": p, "recall": r, "threshold": t}
#                     for p, r, t in prc_points
#                 ]
#             },
#             fd,
#             indent=4,
#         )


#     # ... confusion matrix plot
#     live.log_plot("confusion_matrix", labels.squeeze(), predictions_by_class.argmax(-1))


# # Load model and data.
# with open(model_file, "rb") as fd:
#     model = pickle.load(fd)

# with open(train_file, "rb") as fd:
#     train, feature_names = pickle.load(fd)

# with open(test_file, "rb") as fd:
#     test, _ = pickle.load(fd)

# # Evaluate train and test datasets.
# evaluate(model, train, "train")
# evaluate(model, test, "test")

# # Dump feature importance image and show it with your plots.
# fig, axes = plt.subplots(dpi=100)
# fig.subplots_adjust(bottom=0.2, top=0.95)
# importances = model.feature_importances_
# forest_importances = pd.Series(importances, index=feature_names).nlargest(n=30)
# axes.set_ylabel("Mean decrease in impurity")
# forest_importances.plot.bar(ax=axes)
# fig.savefig(os.path.join("evaluation", "importance.png"))
