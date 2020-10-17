#pip install pyodbc
import pandas as pd
import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=ayurtantra.database.windows.net;"
                      #"Database=Nivano;"
                      #"UID=qcqauser;PWD=Q3Q@Us3r@1234"
                      "Database=AyurDB;"
                      "UID=sadmin;PWD=Niramaya!23"
                      ";MARS_Connection=Yes")

#for windows based authentication
##cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=NIRMAL\SQLEXPRESS;Database=ayurtantra;Trusted_Connection=yes")

cursor = cnxn.cursor()

print ('process started')

cursor.execute('select Fname from Patient_Detail')

for row in cursor.fetchall():
    print (row[0])

#df = pd.concat([chunk for chunk in pd.read_sql ('select * from ADS_Final order by ClaimId asc', con = cnxn, chunksize=1000)], ignore_index= True)

#for chunk in pd.read_sql ('select * from ads_test', con = cnxn, chunksize=10):
#    #print (chunk)
#    df.append(chunk, ignore_index=True)

#df.to_csv('AA_Rule_Suggestion/ads_test.csv',index=False)

print ('exported')

cnxn.close()