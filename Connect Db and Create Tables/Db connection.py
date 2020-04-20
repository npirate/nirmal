#pip install pyodbc
import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=172.16.4.76;"
                      "Database=CLINICASQA;"
                      "UID=SA;PWD=Qu1CkMed@2017")

#for windows based authentication
##cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=NIRMAL\SQLEXPRESS;Database=ayurtantra;Trusted_Connection=yes")

cursor = cnxn.cursor()
cursor.execute('SELECT ClaimNo, * FROM vwClaims WHERE StatementDateFrom <> ServiceFromDate')

for row in cursor.fetchall():
    print (row[0])

cnxn.close()
