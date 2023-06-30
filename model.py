import pickle
from sklearn.ensemble import RandomForestClassifier
import sklearn

print('The scikit-learn version is {}.'.format(sklearn.__version__))

with open('models/model.pkl', 'rb') as f:
    m = pickle.load(f)

def predict(data):
    return m.predict(data)

def predict_proba(data):
    return m.predict_proba(data)