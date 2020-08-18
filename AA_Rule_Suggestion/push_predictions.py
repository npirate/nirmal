import pandas as pd
import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=172.16.0.5;"
                      "Database=Nivano;"
                      "UID=qcqauser;PWD=Q3Q@Us3r@1234"
                      ";MARS_Connection=Yes")

df = pd.read_csv(r'AA_Rule_Suggestion\aarule_predictions.csv', index_col=0)

df = df[['claimid','rule_pred']]

cursor = cnxn.cursor()
print('processing')
#for index,row in df.iterrows():
#    cursor.execute("insert into aaAutoAdjudicationRulesPredicted ([claimno],[AARuleID]) values (?,?)", row['claimid'], row['rule_pred'])
#    cnxn.commit()

df.to_sql('aaAutoAdjudicationRulesPredicted', con = cnxn, if_exists = 'append', chunksize = 1000)

#cursor.close()


print ('data inserted to mssql')

cnxn.close()

