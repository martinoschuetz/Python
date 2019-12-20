import os
import sys

from sas7bdat import SAS7BDAT

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib
import xgboost as xgb


if len(sys.argv) == 3:
    os.chdir(sys.argv[2])
else:
	os.chdir(sys.argv[1])

with SAS7BDAT("train.sas7bdat") as m:
    df_train = m.to_data_frame()

if len(sys.argv) == 3:
    os.chdir(sys.argv[1])
	
vlist = list(df_train.columns.values)

df_train = df_train.apply(lambda x: x.fillna(value= -1) if x.dtypes == np.number else x)
df_train = df_train.apply(lambda x: x.fillna(value= '-1') if x.dtypes == object else x)
df_train = df_train.apply(lambda x: -1 if x.unique()[0] == '-1' and len(x.unique()) == 1 else x)

# Some feature selection
field_disp = np.array(['xxx'])
for a in df_train.columns.values:
    if len(np.unique(df_train[a].dropna())) != 0:
#         print 'Len of ', a ,' = ', len(unique(df_train[a])),
        if df_train[a].dtype == object and len(np.unique(df_train[a])) != 1: 
            field_disp = np.array([a]) if field_disp[0] == 'xxx' else np.append(field_disp,a)
        elif df_train[a].dtype in ['int64','float64'] and df_train[a].std() != 0:
            field_disp = np.array([a]) if field_disp[0] == 'xxx' else np.append(field_disp,a) 

joblib.dump(field_disp, "field_disp.dat")			

df_train = df_train[field_disp]

y_train = df_train['TARGET']
x_train = df_train.drop(['TARGET','ID'], axis=1)

model = xgb.XGBClassifier(
    max_depth=2, eta=0.1, colsample_bytree=0.9, min_child_weight=5,
    colsample_bylevel = 0.9, subsample = 0.8, objective="binary:logistic",
    eval_metric="logloss", nthread=30, alpha=1.0, booster="dart", rate_drop=0.01,
    n_estimators=2).fit(x_train, y_train)

joblib.dump(model, "model.dat")
