import pandas as pd

import matplotlib.pyplot as plt

from matplotlib import interactive
interactive(True)

import statsmodels.api as sm

datafile = pd.read_csv('PredictClaimCounts\Train.csv')
datafile['CreatedDate'] = pd.to_datetime(datafile.CreatedDate,infer_datetime_format=True)
datafile = datafile.set_index('CreatedDate')

train = datafile['2018-06-04':'2019-11-30']
validate = datafile['2019-12-01':'2020-05-21']

sm.tsa.seasonal_decompose(train.Count).plot()