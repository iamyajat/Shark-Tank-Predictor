import pickle
import sklearn

print('Welcome to the Shark Tank Predictor :) \nUsing SciKit version : {}'.format(
    sklearn.__version__))

with open('models/model.pkl', 'rb') as f:
    m = pickle.load(f)


def predict(data):
    return m.predict(data)


def predict_proba(data):
    return m.predict_proba(data)
