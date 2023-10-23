# import os
# from sklearn.datasets import fetch_kddcup99
# data = fetch_kddcup99(download_if_missing=False)

from sklearn.datasets import load_iris
iris = load_iris()

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=1024)

# Train
model.fit(iris.data, iris.target)
estimator = model.estimators_[5]

import pickle
s = pickle.dumps(model)
clf2 = pickle.loads(s)
# Extract single tree
