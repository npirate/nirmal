import pandas as pd
train = pd.read_csv('Train.csv', index_col =0)#using the id column as index
train = train.rename(columns = {'average_runtime(minutes_per_week)':'runtime','realtionship_status':'relationship','targeted_sex':'gender'})#relabelling column names

#dealing with categorical data

import numpy as np
train['netgain'] = np.where(train['netgain'] & True, 1, 0)#converting dependent variable to nominal data

#converting airlocation feature to 0,1
#train['InUSA']=np.where(train['airlocation'] =='United-States', 1, 0)
train = train.drop(['airlocation'], axis = 1)

#converting relationship to spouse_present
train['spouse_present'] = train['relationship'].apply({'Married-AF-spouse':1, 'Married-civ-spouse':1}.get)
train.spouse_present.fillna(0, inplace=True)
train = train.drop(['relationship'], axis = 1)

#doing one hot encoding
train = pd.get_dummies(train,prefix = ['industry', 'genre', 'airtime','gender','expensive','money_back_guarantee'], columns = ['industry', 'genre', 'airtime','gender','expensive','money_back_guarantee'])
train = train.drop(['industry_Other','genre_Direct','airtime_Daytime','gender_Female','expensive_Low','money_back_guarantee_No'], axis = 1)

from sklearn.preprocessing import StandardScaler
#train['normruntime'] = StandardScaler().fit_transform(np.array(train['runtime']).reshape(-1,1))
train['normratings'] = StandardScaler().fit_transform(np.array(train['ratings']).reshape(-1,1))

train = train.drop(['runtime','ratings'], axis = 1)

#selecting features for model fitting
X_train = np.array(train.iloc[:,train.columns !='netgain'])

y_train = np.array(train.iloc[:,train.columns =='netgain'])

#balancing out the training sample

from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=2)
X_train_res, y_train_res = sm.fit_sample(X_train, y_train.ravel())

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor(n_estimators=200, criterion='mse', n_jobs= -1, random_state=2)
# Training the regressor with training data
rfr.fit(X_train_res, y_train_res)


#working with test data

test = pd.read_csv('test.csv', index_col =0)#using the id column as index
test = test.rename(columns = {'average_runtime(minutes_per_week)':'runtime','realtionship_status':'relationship','targeted_sex':'gender'})#relabelling column names

#dealing with categorical data

#converting airlocation feature to 0,1
#test['InUSA']=np.where(test['airlocation'] =='United-States', 1, 0)
test = test.drop(['airlocation'], axis = 1)

#converting relationship to spouse_present
test['spouse_present'] = test['relationship'].apply({'Married-AF-spouse':1, 'Married-civ-spouse':1}.get)
test.spouse_present.fillna(0, inplace=True)
test = test.drop(['relationship'], axis = 1)

#doing one hot encoding
test = pd.get_dummies(test,prefix = ['industry', 'genre', 'airtime','gender','expensive','money_back_guarantee'], columns = ['industry', 'genre', 'airtime','gender','expensive','money_back_guarantee'])
test = test.drop(['industry_Other','genre_Direct','airtime_Daytime','gender_Female','expensive_Low','money_back_guarantee_No'], axis = 1)

from sklearn.preprocessing import StandardScaler
#test['normruntime'] = StandardScaler().fit_transform(np.array(test['runtime']).reshape(-1,1))
test['normratings'] = StandardScaler().fit_transform(np.array(test['ratings']).reshape(-1,1))

test = test.drop(['runtime','ratings'], axis = 1)

X_test = np.array(test)

y_pred = rfr.predict(X_test) #got array of prediction probabilities

y_pred = np.where (y_pred >=0.5, 1 , 0) 

submission = test.index.values #got the ids of the test entries in a list

result_submission = pd.DataFrame(list(zip(submission,y_pred)),columns = ['id','netgain'])#created dataframe as per submission format from lists

result_submission['netgain'] = np.where(result_submission['netgain'] & True, 'true', 'false')#reversing data manipulation

result_submission.to_csv('submission_rfr_2.csv', index = False)#indexes are not copied in the csv

print('Submission is Ready')
