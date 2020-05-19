import pandas as pd
df = pd.read_csv('train.csv', index_col =0)#using the id column as index

df = df.rename(columns = {'average_runtime(minutes_per_week)':'runtime','realtionship_status':'relationship','targeted_sex':'gender'})#relabelling column names

import numpy as np

df['netgain'] = np.where(df['netgain'] & True, 1, 0)#converting dependent variable to nominal data

df['airlocation']=np.where(df['airlocation'] =='Hungary', 'Other', df['airlocation'])

df['airlocation']=np.where(df['airlocation'] =='Outlying-US(Guam-USVI-etc)', 'Other', df['airlocation'])

df['airlocation']=np.where(df['airlocation'] =='Holand-Netherlands', 'Other', df['airlocation'])

#print (df.columns)

#performing one hot encoding

df = pd.get_dummies(df,prefix = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'], columns = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'])
#note that the original columns are removed when get_dummies is used

df.columns.str.strip()

#normalizing data
from sklearn.preprocessing import StandardScaler
df['normruntime'] = StandardScaler().fit_transform(np.array(df['runtime']).reshape(-1,1))
df['normratings'] = StandardScaler().fit_transform(np.array(df['ratings']).reshape(-1,1))

#removing the non-normal columns as they are not useful in predictions now
df = df.drop(['runtime', 'ratings'], axis = 1)

#moving independent columns and dependent column with their values to nparray objects
X = np.array(df.iloc[:,df.columns !='netgain'])#all rows and columns not equal to netgain
y = np.array(df.iloc[:,df.columns =='netgain'])

#train, test * X,y ie splitting data into training and test. This is Hold Out Methd | Another technique is k-fold cross validation
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) #test will be 20% of total set. disadvantage: patterns in test sample will not be incorporated in the model

#over-sampling the training set to take care of the imbalance in y_training data

print("Before OverSampling, counts of netgain as yes : {}".format(sum(y_train==1)))
print("Before OverSampling, counts of netgain as no : {}".format(sum(y_train==0)))

from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=2)
X_train_res, y_train_res = sm.fit_sample(X_train, y_train.ravel())

#print('X_train_oversampled : {}'.format(X_train_res.shape))

#print('y_train_oversampled : {}'.format(y_train_res.shape))

#creating logistic model
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(fit_intercept = False, max_iter=1000) #fit_intercept false takes care of the dummy variable trap.
lr.fit(X_train_res,y_train_res)#model created
print ('Accurancy against derived test data :{}'.format(lr.score(X_test,y_test)))#test data passed to find accuracy of the model. X_test will be used to predict and predicted values will be compared with y_test and accurany checked.

from sklearn.metrics import classification_report
y_pred = lr.predict(X_test)#use input (X_test) in same format as used to create model to predict output
print(classification_report(y_test, y_pred))
