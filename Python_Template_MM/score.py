import os
import sys

from sas7bdat import SAS7BDAT

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib
import xgboost as xgb


if len(sys.argv) > 1:
    os.chdir(sys.argv[1])

model = joblib.load("model.dat")
field_disp = joblib.load("field_disp.dat")
#transformers = joblib.load("transformers.dat")

if len(sys.argv) == 3:
    os.chdir(sys.argv[2])

with SAS7BDAT("score.sas7bdat") as m:
    df_test = m.to_data_frame()

vlist = list(df_test.columns.values)
	
df_test = df_test.apply(lambda x: x.fillna(value= -1) if x.dtypes == np.number else x)
df_test = df_test.apply(lambda x: x.fillna(value= '-1') if x.dtypes == object else x)
df_test = df_test.apply(lambda x: -1 if x.unique()[0] == '-1' and len(x.unique()) == 1 else x)

df_test = df_test[field_disp]

#for a in vlist:
#    df_test[a] = transformers[a].transform(df_test[a])

y_test = df_test['TARGET']
x_test = df_test.drop(['TARGET','ID'], axis=1)

y_proba = model.predict_proba(x_test)[:,1]
with open("predict.csv", "w") as f:
    f.write("P_TARGET\n")
    f.write("\n".join([str(proba) for proba in y_proba]))
