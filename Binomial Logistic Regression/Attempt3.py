import pandas as pd
train = pd.read_csv('Train.csv', index_col =0)#using the id column as index
train = train.rename(columns = {'average_runtime(minutes_per_week)':'runtime','realtionship_status':'relationship','targeted_sex':'gender'})#relabelling column names

import numpy as np
train['netgain'] = np.where(train['netgain'] & True, 1, 0)#converting dependent variable to nominal data

#merging low frequency categorial data in single group

train['airlocation']=np.where(train['airlocation'] =='Hungary', 'Other', train['airlocation'])
train['airlocation']=np.where(train['airlocation'] =='Outlying-US(Guam-USVI-etc)', 'Other', train['airlocation'])
train['airlocation']=np.where(train['airlocation'] =='Holand-Netherlands', 'Other', train['airlocation'])
#print (train.airlocation.value_counts())

###ST merging all married people. Did as part of 3rd submission. worsened.
##
##train['relationship'] = np.where(train['relationship'] == 'Married-AF-spouse','Married',train['relationship'])
##train['relationship'] = np.where(train['relationship'] == 'Married-civ-spouse','Married',train['relationship'])
##train['relationship'] = np.where(train['relationship'] == 'Married-spouse-absent','Married',train['relationship'])
##print (train.relationship.value_counts())
###SE

#doing one hot encoding
train = pd.get_dummies(train,prefix = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'], columns = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'])

print (train.columns)
from sklearn.preprocessing import StandardScaler
train['normruntime'] = StandardScaler().fit_transform(np.array(train['runtime']).reshape(-1,1))
train['normratings'] = StandardScaler().fit_transform(np.array(train['ratings']).reshape(-1,1))

train = train.drop(['runtime', 'ratings'], axis = 1)

#ST 4th submission
#train = train.drop(['airlocation_Other','runtime', 'ratings','relationship_Married-civ-spouse','industry_Pharma','genre_Comedy','gender_Female','airtime_Morning','expensive_High','money_back_guarantee_No'], axis = 1)
#SE

X_train = np.array(train.iloc[:,train.columns !='netgain'])

y_train = np.array(train.iloc[:,train.columns =='netgain'])

from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=2)
X_train_res, y_train_res = sm.fit_sample(X_train, y_train.ravel())

from sklearn.linear_model import LogisticRegression
#ST 4th submission
#lr = LogisticRegression(max_iter=1000)

lr = LogisticRegression(fit_intercept = False, max_iter=1000)

#SE
lr.fit(X_train_res,y_train_res)

test = pd.read_csv('Test.csv', index_col =0)
test = test.rename(columns = {'average_runtime(minutes_per_week)':'runtime','realtionship_status':'relationship','targeted_sex':'gender'})


test['airlocation']=np.where(test['airlocation'] =='Hungary', 'Other', test['airlocation'])
test['airlocation']=np.where(test['airlocation'] =='Outlying-US(Guam-USVI-etc)', 'Other', test['airlocation'])

###ST 3rd submission. worsened.
##
##test['relationship'] = np.where(test['relationship'] == 'Married-AF-spouse','Married',test['relationship'])
##test['relationship'] = np.where(test['relationship'] == 'Married-civ-spouse','Married',test['relationship'])
##test['relationship'] = np.where(test['relationship'] == 'Married-spouse-absent','Married',test['relationship'])
##
###SE

test = pd.get_dummies(test,prefix = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'], columns = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'])
#note that the original columns are removed when get_dummies is used

test['normruntime'] = StandardScaler().fit_transform(np.array(test['runtime']).reshape(-1,1))
test['normratings'] = StandardScaler().fit_transform(np.array(test['ratings']).reshape(-1,1))

##ST 4th submission
#test = test.drop(['airlocation_Other','runtime', 'ratings','relationship_Married-civ-spouse','industry_Pharma','genre_Comedy','gender_Female','airtime_Morning','expensive_High','money_back_guarantee_No'], axis = 1)

test = test.drop(['runtime', 'ratings'], axis = 1)

##SE

X_test = np.array(test)

y_pred = lr.predict(X_test) #got list of predictions

submission = test.index.values #got the ids of the test entries in a list

result_submission = pd.DataFrame(list(zip(submission,y_pred)),columns = ['id','netgain'])#created dataframe as per submission format from lists

result_submission['netgain'] = np.where(result_submission['netgain'] & True, 'true', 'false')#reversing data manipulation

result_submission.to_csv('submission1.csv', index = False)#indexes are not copied in the csv

print('Submission is Ready')
