import numpy as np
import pandas as pd

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler


from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from statsmodels.regression.linear_model import OLS

from imblearn.over_sampling import SMOTE

def scaler(X_train, X_test, minmax = False):
    if minmax == True:
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled

def get_indices(df):
    X_full_indices = df.drop(['pt_suc', 'pt_attempt'], axis =1 ).columns
    return X_full_indices


def splitter(df, target = 'pt_attempt', test_size = .25, random_state = 29, VIF_drop = False, scaled = False, minmax = False):
    _targets = ['pt_attempt', 'pt_suc']
    df = add_constant(df)
    indices = get_indices(df)
    if VIF_drop == True:
        df = df.drop(vifdrops, axis = 1)
        y = df[target]
        X = df.drop(_targets, axis = 1)
    if VIF_drop == False:
        y = df[target]
        X = df.drop(_targets, axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= test_size, random_state= random_state, stratify = y )
    if scaled == True:
        X_train, X_test = scaler(X_train, X_test, minmax = minmax)
    return X_train, X_test, y_train, y_test, indices

def upsampler(X_train, y_train, target = 'pt_attempt'):
    X = pd.concat([X_train, y_train], axis=1) 
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
    X = pd.concat([X_train, y_train], axis=1) 
    no_coup = X[X[target]==0]
    coup = X[X[target]==1]
    coups_downsampled = resample(no_coup,
                          replace=True, # sample with replacement
                          n_samples=len(coup), # match number in majority class
                          random_state=29)
    downsampled = pd.concat([coup, coups_downsampled])
    y_down = downsampled[target]
    X_down = downsampled.drop(target, axis = 1)
    return X_down, y_down

def smoter(X_train, y_train, ratio = 1.0):
    sm = SMOTE(random_state=29, ratio=ratio)
    X_train_sm, y_train_sm = sm.fit_sample(X_train, y_train)
    return X_train_sm, y_train_sm


def variance_inflation_factors(X):
    # X = add_constant(X)
    vifs = pd.Series(
        [1 / (1. - OLS(X[col].values, 
                       X.loc[:, X.columns != col].values).fit().rsquared) 
         for col in X],
        index=X.columns,
        name='VIF'
    )
    return vifs.sort_values()


def data_pipeline(df, target = 'pt_attempt', test_size = .25, random_state = 29, VIF_drop = False, scaled = False, minmax = False, resampler = None, sample_ratio = 1):
    X_train, X_test, y_train, y_test, indices = splitter(df, target = 'pt_attempt', test_size = .25, 
                                                random_state = 29, VIF_drop = VIF_drop, scaled = scaled, minmax = minmax)
    if resampler == 'upsample':
        X_train, y_train = upsampler(X_train, y_train)
    if resampler == 'downsample':
        X_train, y_train = downsampler(X_train, y_train)
    if resampler == 'smote':
        X_train, y_train = smoter(X_train, y_train, ratio = sample_ratio)
    return X_train, X_test, y_train, y_test, indices

def get_feature_weights(model, indices):
    d_log_vals = {}
    for idx, feat in enumerate(model.coef_[0]):
        d_log_vals[indices[idx]] = feat  
    s_log_vals = (pd.Series(d_log_vals)).sort_values()
    return s_log_vals

def metric_test(model, X_test, y_test):
    preds = model.predict(X_test)
    print('accuracy = ' + str(accuracy_score(y_test, preds)))
    print('recall = ' + str(recall_score(y_test, preds)))
    print('precision = ' + str(precision_score(y_test, preds)))
    print('f1 score = ' + str(f1_score(y_test, preds)))
    print('accuracy + recall = ' + str(accuracy_score(y_test, preds) + recall_score(y_test, preds)))

def fit_test_model(model, X_train, X_test, y_train, y_test, indices, do_metric_test = True, get_features = False):
    model.fit(X_train, y_train)
    if do_metric_test == True:
        metric_test(model, X_test, y_test)
    if get_features == True:
        features = get_feature_weights(model, indices)
        print(features)
    return model


if __name__ == '__main__':

    df = pd.read_pickle('../data/pickles/df_one_hot_num.pkl')


    #these were determined through looking at VIF outputs and removing one member of pairs that seemed correlated
    vifdrops = ['election_recent', 'imports', 'exports', 'victory_recent', 'upop', 'direct_recent', 'leg_recent', 'pec', 'anticipation', 'cinc', 'lead_recent']


    # df_const = 
    # df_vif = df.drop(VIFdrops, axis =1 )
    # X_full_indices = df.drop(['pt_suc', 'pt_attempt'], axis =1 ).columns
    # X_vif_indices = df_vif.drop(['pt_suc', 'pt_attempt'], axis =1 ).columns

    # toy_model = LogisticRegressionCV(
    #     cv=2, dual=False,
    #     penalty='l2', 
    #     scoring='recall',
    #     solver='saga', 
    #     n_jobs = 2,
    #     tol=0.0001,
    #     max_iter=100,)

    ridge_scaled = LogisticRegressionCV(
        cv=5, dual=False,
        penalty='elasticnet', 
        scoring='recall',
        solver='saga', 
        n_jobs = 2,
        tol=0.0001,
        max_iter=100,
        l1_ratios = [0, .5, 1])

   

    X_train, X_test, y_train, y_test, indices = data_pipeline(df, target='pt_attempt', test_size = .25, random_state = 29, VIF_drop = True, scaled = True, resampler = 'smote', sample_ratio = 1)
    fit_test_model(ridge_scaled, X_train, X_test, y_train, y_test, indices, get_features = True)



   
    

