#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mutual_info_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import roc_auc_score
import xgboost as xgb
import bentoml

df = pd.read_csv('employee-attrition.csv')

df.columns = df.columns.str.lower()

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

y_full_train = (df.attrition == 'yes').astype('int').values

del df['attrition']

dict_full_train = df.to_dict(orient='records')

dv = DictVectorizer(sparse=False)

X_train = dv.fit_transform(dict_full_train)
features = dv.get_feature_names_out()
dtrain = xgb.DMatrix(X_train, label=y_full_train)


watchlist = [(dtrain, 'train')]
xgb_params = {
    'eta': 0.1,
    'max_depth': 3,
    'min_child_weight': 1,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 8,
    'seed': 1,
}

model = xgb.train(xgb_params, dtrain,
                  num_boost_round=170, verbose_eval=10,
                  evals=watchlist)


bentoml.xgboost.save_model(
    'employee_attrition',
    model,
    custom_objects={
        'dictVectorizer': dv
    })






