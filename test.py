from sklearn import svm
from sklearn import datasets
import pickle
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)  

from sklearn.externals import joblib
joblib.dump(clf, 'output.txt', compress=1)