#import pandas as pd
#df = pd.read_csv('sftp_details.csv',names = ['client','company','host','username','password','port','chdir'],header=0)
#print (df)
    
## pip install pysftp
import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
print ('hostkeys set as none')

##delete local log file
import os
os.remove('log_file.log')

for i in range (0,1):
    try:
        with pysftp.Connection(host = '172.16.4.76', username='quickba', password='m3dic0p@009', cnopts = cnopts, log = 'log_file.log' ) as sftp:#India QA
            print ('connected')
            try:
                sftp.chdir('CLINICASQA')
            except:
                #sftp.mkdir('QCBA_Query')
                #sftp.chdir('QCBA_Query')
                #with sftp.cd('public'):        # temporarily chdir to public
                print ('company db not found.')
            sftp.put('sample.txt')  # upload file to current working remote directory
                #sftp.get('remote_file')         # get a remote file
        print ('File placed successfully')
    except:
        print ('not connected')

    
#with pysftp.Connection('207.178.145.106', username='medvision', password='M3dv1sion', cnopts = cnopts, port = 2222, log = 'log_file.log') as sftp:#clinicas

#update local log file to indicate renewed connection attempt
