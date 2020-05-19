import pandas as pd
train = pd.read_csv('Train.csv', index_col =0)#using the id column as index
train = train.rename(columns = {'average_runtime(minutes_per_week)':'runtime','realtionship_status':'relationship','targeted_sex':'gender'})#relabelling column names

import numpy as np
train['netgain'] = np.where(train['netgain'] & True, 1, 0)#converting dependent variable to nominal data

train = train.drop(['airlocation','runtime'], axis = 1)

train['spouse_present'] = train['relationship'].apply({'Married-AF-spouse':1, 'Married-civ-spouse':1}.get)
train.spouse_present.fillna(0, inplace=True)

train['expensive_moneyback'] = np.where((train['expensive'] == 'High') & (train['money_back_guarantee'] == 'Yes'), 1, 0)

#doing one hot encoding
train = pd.get_dummies(train,prefix = ['industry', 'genre', 'gender', 'airtime'], columns = ['industry', 'genre', 'gender', 'airtime'])

#print (train.columns)
from sklearn.preprocessing import StandardScaler
#train['normruntime'] = StandardScaler().fit_transform(np.array(train['runtime']).reshape(-1,1))
train['normratings'] = StandardScaler().fit_transform(np.array(train['ratings']).reshape(-1,1))

#dropping one dummy variable of each feature to avoid dummy variable trap
train = train.drop(['ratings','relationship','industry_Other','genre_Direct','gender_Female','airtime_Daytime','expensive','money_back_guarantee'], axis = 1)

print (train.columns)

X_train = np.array(train.iloc[:,train.columns !='netgain'])

y_train = np.array(train.iloc[:,train.columns =='netgain'])

from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=2)
X_train_res, y_train_res = sm.fit_sample(X_train, y_train.ravel())

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(max_iter=1000)

lr.fit(X_train_res,y_train_res)

test = pd.read_csv('Test.csv', index_col =0)
test = test.rename(columns = {'average_runtime(minutes_per_week)':'runtime','realtionship_status':'relationship','targeted_sex':'gender'})


test = test.drop(['airlocation','runtime'], axis = 1)

test['spouse_present'] = test['relationship'].apply({'Married-AF-spouse':1, 'Married-civ-spouse':1}.get)
test.spouse_present.fillna(0, inplace=True)

test['expensive_moneyback'] = np.where((test['expensive'] == 'High') & (test['money_back_guarantee'] == 'Yes'), 1, 0)

#doing one hot encoding
test = pd.get_dummies(test,prefix = ['industry', 'genre', 'gender', 'airtime'], columns = ['industry', 'genre', 'gender', 'airtime'])

#print (train.columns)
from sklearn.preprocessing import StandardScaler
#train['normruntime'] = StandardScaler().fit_transform(np.array(train['runtime']).reshape(-1,1))
test['normratings'] = StandardScaler().fit_transform(np.array(test['ratings']).reshape(-1,1))

#dropping one dummy variable of each feature to avoid dummy variable trap
test = test.drop(['ratings','relationship','industry_Other','genre_Direct','gender_Female','airtime_Daytime','expensive','money_back_guarantee'], axis = 1)

X_test = np.array(test)

y_pred = lr.predict(X_test) #got list of predictions

submission = test.index.values #got the ids of the test entries in a list

result_submission = pd.DataFrame(list(zip(submission,y_pred)),columns = ['id','netgain'])#created dataframe as per submission format from lists

result_submission['netgain'] = np.where(result_submission['netgain'] & True, 'true', 'false')#reversing data manipulation

result_submission.to_csv('submission8.csv', index = False)#indexes are not copied in the csv

print('Submission is Ready')
