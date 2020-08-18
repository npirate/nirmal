#pip install pyodbc
import pandas as pd
import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=172.16.0.5;"
                      "Database=Nivano;"
                      "UID=qcqauser;PWD=Q3Q@Us3r@1234"
                      ";MARS_Connection=Yes")

#for windows based authentication
##cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=NIRMAL\SQLEXPRESS;Database=ayurtantra;Trusted_Connection=yes")

cursor = cnxn.cursor()
#cursor.execute('select * from ads_test')

#for row in cursor.fetchall():
#    print (row[0])

print ('process started')

df = pd.concat([chunk for chunk in pd.read_sql ('select * from ADS_Final order by ClaimId asc', con = cnxn, chunksize=1000)], ignore_index= True)

#for chunk in pd.read_sql ('select * from ads_test', con = cnxn, chunksize=10):
#    #print (chunk)
#    df.append(chunk, ignore_index=True)

df.to_csv('AA_Rule_Suggestion/ads_final.csv',index=False)

print ('exported')

cnxn.close()