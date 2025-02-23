import pickle
import joblib
import pandas as pd
import os

# get current working directory
cwd = os.path.dirname(__file__)


def save_processed_data(data):
    with open(f'{cwd}/data/data.pickle', 'wb') as file:
        pickle.dump(data, file)


def load_precessed_data():
    return pd.read_pickle(f'{cwd}/data/data.pickle')


def load_five_columns():
    return pd.read_pickle(f'{cwd}/data/five_features.pickle')


def save_model(model):
    joblib.dump(model, f'{cwd}/data/{model}')


def load_model():
    return joblib.load(f'{cwd}/data/model')

