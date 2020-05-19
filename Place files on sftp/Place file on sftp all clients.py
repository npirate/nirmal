import pandas as pd
df = pd.read_csv('sftp_details.csv',names = ['client','company','host','username','password','port','chdir'],header=0)
#print (df)
    
## pip install pysftp
import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
print ('hostkeys set as none')

##delete local log file
import os
os.remove('log_file.log')

for i in range (0,len(df)):
    try:
        with pysftp.Connection(host = str(df.iloc[i]['host']), username=str(df.iloc[i]['username']), password=str(df.iloc[i]['password']), cnopts = cnopts, log = 'log_file.log', port = int(df.iloc[i]['port'])) as sftp:#India QA
            print ('''{} client's {} company's sftp connected'''.format(df.iloc[i]['client'],df.iloc[i]['company']))
            try:
                sftp.chdir(str(df.iloc[i]['chdir']))
            except:
                sftp.mkdir(str(df.iloc[i]['chdir']))
                sftp.chdir(str(df.iloc[i]['chdir']))
                #with sftp.cd('public'):        # temporarily chdir to public
                 #   print ('test directory created')
            sftp.put('sample.txt')  # upload file to current working remote directory
                #sftp.get('remote_file')         # get a remote file
        print ('File placed successfully')
    except:
        print ('''{} client's {} company's sftp is not connected'''.format(df.iloc[i]['client'],df.iloc[i]['company']))

    
#with pysftp.Connection('207.178.145.106', username='medvision', password='M3dv1sion', cnopts = cnopts, port = 2222, log = 'log_file.log') as sftp:#clinicas

#update local log file to indicate renewed connection attempt
