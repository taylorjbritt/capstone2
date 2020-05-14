import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

def splitter(df, target = 'pt_attempt', test_size = .25, random_state = 29):
    _targets = ['pt_attempt', 'pt_suc']
    y = df[target]
    X = df.drop(_targets, axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size= test_size, random_state= random_state, stratify = y )
    return X_train, X_test, y_train, y_test



def rf_model(df):
    clf = RandomForestClassifier(max_depth=2, random_state=0)






if __name__ == '__main__':
    df = pd.read_pickle('../data/pickles/df_one_hot_num.pkl')
    X_train, X_test, y_train, y_test = splitter(df, target = 'pt_attempt', test_size = .25, random_state = 29)

