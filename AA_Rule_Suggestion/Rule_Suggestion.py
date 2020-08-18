import pandas as pd

#setting rows to show in IDE
pd.set_option('display.max_rows', 500)

#reading ADS
dff = pd.read_csv('ads_final.csv', index_col=0)

#filtering ADS to get df of auto-adjudicated claims
df = dff[dff.IsAA == 1]

#getting frequency distribution of aa rules
df['aaruleid'].value_counts().to_csv('rulefreq.csv')

#identifying rules whose frequency is less than 95% and hence these claims will be removed from ADS. We should try and do this in SQL itself
erulelist = ['Rule:MC1','Rule:MC2','Rule:MC0','Rule:PE1','Rule9140','Rule6002','Rule9107','Rule9133','Rule9117','Rule8008','Rule8020','Rule8010','Rule8017','Rule6001','Rule9102','Rule9151','Rule8007','Rule7004','Rule9136','Rule8006','Rule9108','Rule9135','Rule9120','Rule9142','Rule7003','Rule8024','Rule7002','Rule9109','Rule9138','Rule9147','Rule9104','Rule9144','Rule9139','Rule9143','Rule9118','Rule9134','Rule9130','Rule9132','Rule9112','Rule9149','Rule9124','Rule9111','Rule9114','Rule9110','Rule9101','Rule9116','Rule9125']

#defining function to identify claims that need to be removed
def flag_col (col_name):
    x = 0
    x = 1 if col_name in erulelist else x
    return x

df['remove'] = df.apply(lambda x: flag_col(x.aaruleid), axis = 1)

#filtering and hence removing rows that need to be removed by including those that need not be removed.
df = df[df.remove == 0]

#binning count of service lines
bins = [0,1,2,50]
labels = [1,2,3]
df['CNT_SERVICE_LINES_BINNED'] = pd.cut(df['CNT_SERVICE_LINES'], bins=bins, labels=labels)

#checking for null values in the ADS after processing.
df.isnull().sum()

#encoding the labels
import sklearn
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
df['aaruleid_enc'] = label_encoder.fit_transform(df['aaruleid'])

#saving and exporting encoding information

keys = label_encoder.classes_
values = label_encoder.transform(label_encoder.classes_)
rule_dict = dict(zip(keys,values))
#code for exporting the rule_dict

#hot encoding of categorical columns

df.dtypes

df = pd.get_dummies(df, prefix=['PlaceOfServiceCode','HPBC','ProvSpeciltyCode','Provider_Type','PROV_CONTRACT_TYPE','NetworkStatus','CNT_SERVICE_LINES_BINNED'], columns= ['PlaceOfServiceCode','HPBC','ProvSpeciltyCode','Provider_Type','PROV_CONTRACT_TYPE','NetworkStatus','CNT_SERVICE_LINES_BINNED'])

#df.to_csv('test_2.csv')

#splitting ADS into X and y

#selcting columns for y
y = df[['aaruleid_enc']]

#selecting columns for X
df.dtypes
df.columns.values

X = df[['AuthNo','IsPCPClaim','IsCoordinationOfBenefits','Gender','Benefit_Rule_Count','PositiveNet','PositivePR','adj_PO13','adj_MCAL','adj_MCAR','adj_P14','adj_15','adj_COB','adj_NMCAL','adj_149','adj_246','C4','C5','C11','C9','C10','C12','C13','C14','C18','C19','C21','C6','C1','PlaceOfServiceCode_2','PlaceOfServiceCode_11','PlaceOfServiceCode_20','PlaceOfServiceCode_21','PlaceOfServiceCode_22','PlaceOfServiceCode_23','PlaceOfServiceCode_72','PlaceOfServiceCode_81','HPBC_ATMC60','HPBC_ATMCM1','HPBC_ATMCM3','HPBC_BC10','HPBC_BC1H','HPBC_BC30','HPBC_BC32','HPBC_BC35','HPBC_BC60','HPBC_BC6E','HPBC_BC6H','HPBC_BCK1','HPBC_BCL6','HPBC_BCM1','HPBC_BCM3','HPBC_BCM5','HPBC_BCM7','HPBC_BCP5','HPBC_BCP7','HPBC_BCP9','HPBC_BCT1','HPBC_BCT2','HPBC_BCT3','HPBC_MOL60','HPBC_MOLM1','HPBC_MOLM3','ProvSpeciltyCode_AI','ProvSpeciltyCode_AN','ProvSpeciltyCode_CRD','ProvSpeciltyCode_D','ProvSpeciltyCode_DME','ProvSpeciltyCode_EM','ProvSpeciltyCode_FNP','ProvSpeciltyCode_FP','ProvSpeciltyCode_GE','ProvSpeciltyCode_GS','ProvSpeciltyCode_HOS','ProvSpeciltyCode_IM','ProvSpeciltyCode_LAB','ProvSpeciltyCode_MS','ProvSpeciltyCode_N','ProvSpeciltyCode_NP','ProvSpeciltyCode_OBG','ProvSpeciltyCode_OPH','ProvSpeciltyCode_ORS','ProvSpeciltyCode_OTO','ProvSpeciltyCode_P','ProvSpeciltyCode_PAI','ProvSpeciltyCode_PD','ProvSpeciltyCode_PDP','ProvSpeciltyCode_POD','ProvSpeciltyCode_PP','ProvSpeciltyCode_PT','ProvSpeciltyCode_R','ProvSpeciltyCode_SM','ProvSpeciltyCode_U','ProvSpeciltyCode_US','Provider_Type_7','Provider_Type_AH','Provider_Type_H','Provider_Type_HB','PROV_CONTRACT_TYPE_1','PROV_CONTRACT_TYPE_2','PROV_CONTRACT_TYPE_3','PROV_CONTRACT_TYPE_4','PROV_CONTRACT_TYPE_5','PROV_CONTRACT_TYPE_6','PROV_CONTRACT_TYPE_7','PROV_CONTRACT_TYPE_8','PROV_CONTRACT_TYPE_10','NetworkStatus_1','CNT_SERVICE_LINES_BINNED_1','CNT_SERVICE_LINES_BINNED_2','CNT_SERVICE_LINES_BINNED_3']]

#undersampling the imbalanced dataset
from imblearn.under_sampling import RandomUnderSampler
rus = RandomUnderSampler(random_state = 0)
X_res, y_res = rus.fit_resample(X,y)

#creating train-test dataset
from sklearn.model_selection import train_test_split
train_X_res, test_X_res, train_y_res, test_y_res = train_test_split(X_res, y_res, test_size=0.25, random_state=2)

#training model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5).fit(train_X_res, train_y_res.values.ravel())

#using model to make predictions on test
knn_predictions = knn.predict(test_X_res)

#checking accuracy of model. Here predictions are done again and predictions are compared with actual data.
accuracy = knn.score(test_X_res, test_y_res)

#confusion matrix and classification report
from sklearn.metrics import confusion_matrix, classification_report
cm = confusion_matrix(test_y_res, knn_predictions)
print (classification_report(test_y_res, knn_predictions))

#get ads_pred and repeating data treatment. 

#dfp = pd.read_csv('ads_topredict_final.csv', index_col=0)
dfp = dff[dff.IsAA == 0]

dfp['CNT_SERVICE_LINES_BINNED'] = pd.cut(dfp['CNT_SERVICE_LINES'], bins = bins, labels = labels)

dfp = pd.get_dummies(dfp, prefix=['PlaceOfServiceCode','HPBC','ProvSpeciltyCode','Provider_Type','PROV_CONTRACT_TYPE','NetworkStatus','CNT_SERVICE_LINES_BINNED'], columns= ['PlaceOfServiceCode','HPBC','ProvSpeciltyCode','Provider_Type','PROV_CONTRACT_TYPE','NetworkStatus','CNT_SERVICE_LINES_BINNED'])

X_p = dfp[['AuthNo','IsPCPClaim','IsCoordinationOfBenefits','Gender','Benefit_Rule_Count','PositiveNet','PositivePR','adj_PO13','adj_MCAL','adj_MCAR','adj_P14','adj_15','adj_COB','adj_NMCAL','adj_149','adj_246','C4','C5','C11','C9','C10','C12','C13','C14','C18','C19','C21','C6','C1','PlaceOfServiceCode_2','PlaceOfServiceCode_11','PlaceOfServiceCode_20','PlaceOfServiceCode_21','PlaceOfServiceCode_22','PlaceOfServiceCode_23','PlaceOfServiceCode_72','PlaceOfServiceCode_81','HPBC_ATMC60','HPBC_ATMCM1','HPBC_ATMCM3','HPBC_BC10','HPBC_BC1H','HPBC_BC30','HPBC_BC32','HPBC_BC35','HPBC_BC60','HPBC_BC6E','HPBC_BC6H','HPBC_BCK1','HPBC_BCL6','HPBC_BCM1','HPBC_BCM3','HPBC_BCM5','HPBC_BCM7','HPBC_BCP5','HPBC_BCP7','HPBC_BCP9','HPBC_BCT1','HPBC_BCT2','HPBC_BCT3','HPBC_MOL60','HPBC_MOLM1','HPBC_MOLM3','ProvSpeciltyCode_AI','ProvSpeciltyCode_AN','ProvSpeciltyCode_CRD','ProvSpeciltyCode_D','ProvSpeciltyCode_DME','ProvSpeciltyCode_EM','ProvSpeciltyCode_FNP','ProvSpeciltyCode_FP','ProvSpeciltyCode_GE','ProvSpeciltyCode_GS','ProvSpeciltyCode_HOS','ProvSpeciltyCode_IM','ProvSpeciltyCode_LAB','ProvSpeciltyCode_MS','ProvSpeciltyCode_N','ProvSpeciltyCode_NP','ProvSpeciltyCode_OBG','ProvSpeciltyCode_OPH','ProvSpeciltyCode_ORS','ProvSpeciltyCode_OTO','ProvSpeciltyCode_P','ProvSpeciltyCode_PAI','ProvSpeciltyCode_PD','ProvSpeciltyCode_PDP','ProvSpeciltyCode_POD','ProvSpeciltyCode_PP','ProvSpeciltyCode_PT','ProvSpeciltyCode_R','ProvSpeciltyCode_SM','ProvSpeciltyCode_U','ProvSpeciltyCode_US','Provider_Type_7','Provider_Type_AH','Provider_Type_H','Provider_Type_HB','PROV_CONTRACT_TYPE_1','PROV_CONTRACT_TYPE_2','PROV_CONTRACT_TYPE_3','PROV_CONTRACT_TYPE_4','PROV_CONTRACT_TYPE_5','PROV_CONTRACT_TYPE_6','PROV_CONTRACT_TYPE_7','PROV_CONTRACT_TYPE_8','PROV_CONTRACT_TYPE_10','NetworkStatus_1','CNT_SERVICE_LINES_BINNED_1','CNT_SERVICE_LINES_BINNED_2','CNT_SERVICE_LINES_BINNED_3']]

#using model to make predictions

final_predictions = knn.predict(X_p)

#getting index of live data
get_index = dfp.index.values

#creating dataframe
result_df = pd.DataFrame(list(zip(get_index,final_predictions)),columns = ['claimid','rule_pred_enc'])

#Transform labels back to original encoding.
result_df['rule_pred'] = label_encoder.inverse_transform(result_df['rule_pred_enc'])

#can drop unnecessary columns
result_df = result_df[['claimid','rule_pred']]

#export results to csv or add it back to database
result_df.to_csv('aarule_predictions.csv',index = False)

result_df.rule_pred.value_counts()