import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.utils import resample
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from statsmodels.regression.linear_model import OLS
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE


def splitter(df, target = 'pt_attempt', test_size = .25, random_state = 29):
    _targets = ['pt_attempt', 'pt_suc']
    y = df[target]
    X = df.drop(_targets, axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size= test_size, random_state= random_state, stratify = y )
    return X_train, X_test, y_train, y_test

def metric_test(model, X_test, y_test):
    preds = model.predict(X_test)
    print('accuracy = ' + str(accuracy_score(y_test, preds)))
    print('recall = ' + str(recall_score(y_test, preds)))
    print('precision = ' + str(precision_score(y_test, preds)))
    print('f1 score = ' + str(f1_score(y_test, preds)))

def upsampler(X_train, y_train, target = 'pt_attempt'):
    no_coup = X[X[target]==0]
    coup = X[X[target]==1]
    coups_upsampled = resample(coup,
                          replace=True, # sample with replacement
                          n_samples=len(no_coup), # match number in majority class
                          random_state=29)
    upsampled = pd.concat([no_coup, coups_upsampled])
    y_up = upsampled[target]
    X_up = upsampled.drop(target, axis = 1)
    return X_up, y_up

def downsampler(X_train, y_train, target = 'pt_attempt'):
    no_coup = X[X[target]==0]
    coup = X[X[target]==1]
    coups_upsampled = resample(no_coup,
                          replace=True, # sample with replacement
                          n_samples=len(coup), # match number in majority class
                          random_state=29)
    downsampled = pd.concat([no_coup, coups_upsampled])
    y_down = upsampled[target]
    X_down = upsampled.drop(target, axis = 1)
    return X_down, y_down

def smoter(X_train, y_train, ratio = 1.0):
    sm = SMOTE(random_state=29, ratio=ratio)
    X_train_sm, y_train_sm = sm.fit_sample(X_train, y_train)
    return X_train_sm, y_train_sm

def variance_inflation_factors(X):

    X = add_constant(X)
    vifs = pd.Series(
        [1 / (1. - OLS(X[col].values, 
                       X.loc[:, X.columns != col].values).fit().rsquared) 
         for col in X],
        index=X.columns,
        name='VIF'
    )
    return vifs.sort_values()

#these were determined through looking at VIF outputs and removing one member of pairs that seemed correlated
VIFdrops = ['election_recent', 'imports', 'exports', 'victory_recent', 'upop', 'direct_recent', 'leg_recent', 'pec', 'anticipation', 'cinc', 'lead_recent']

def get_feature_weights(model, X_train):
    d_log_vals = {}
    for idx, feat in enumerate(model.coef_[0]):
        d_log_vals[str(X_train.columns[idx])] = feat  
    s_log_vals = (pd.Series(d_log_vals)).sort_values()






if __name__ == '__main__':

    df = pd.read_pickle('../data/pickles/df_one_hot_num.pkl')
    X_const = add_constant(df)
    X_train, X_test, y_train, y_test = splitter(X_const, target = 'pt_attempt', test_size = .25, random_state = 29)

