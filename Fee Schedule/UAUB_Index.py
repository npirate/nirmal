import pandas #pip install pandas
import numpy
#filedata = pandas.read_csv("feb16_uaub.csv", names = ['OP Code From','OP Code To','OP UA Rate','OP UB Rate','','','IP Code From','IP Code To','IP UA Rate','IP UB Rate'], skiprows=2)
filedata = pandas.read_csv("feb16_uaub.csv", skiprows=2)
#filedata.dropna(inplace = True)
##data = numpy.array(['a','b','c','d'])
##s = pandas.Series(data,index=[100,101,102,103])
##print (s)

#get names of columns of a dataframe

#print (filedata['From'])

#filedata['op comparison'] = numpy.where(filedata['From']==filedata['Thru'],'True','False')

#filedata['From'].str.split('',1)

#filedata['op from 4'] = filedata['From'].str[1:]

#print (filedata['op from 4'])


#print (filedata.columns.values)
##['From' 'Thru' 'UA' 'UB' 'Unnamed: 4' 'Unnamed: 5' 'From.1' 'Thru.1'
## 'UA.1' 'UB.1' 'Unnamed: 10' 'UB - Medicaid level of care 11']

outpatient_df = filedata[['From','Thru','UA','UB']]
outpatient_df['POS'] = 'OP'

inpatient_df = filedata[['From.1','Thru.1','UA.1','UB.1']]
inpatient_df.columns = ['From','Thru','UA','UB']
inpatient_df['POS'] = 'IP'

df = pandas.concat([outpatient_df, inpatient_df],ignore_index = True)
#print (df)
df['Difference'] = numpy.where(df['From'] == df['Thru'],0,df['Thru'].str[1:].apply(pandas.to_numeric) - df['From'].str[1:].apply(pandas.to_numeric)+1)

new_list = []

for row in df.itertuples():
    if row.Difference > 0:
        for i in range (0,int(row.Difference)):
            code = numpy.base_repr(int(row.From,36) + i,36)
            new_list.append([code,code,row.UA,row.UB,row.POS])
    else:
        new_list.append([row.From,row.From,row.UA,row.UB,row.POS])

df = pandas.DataFrame (new_list)

uaub_ip = set(df.loc[df[4] == 'IP',0].tolist())

uaub_op = set(df.loc[df[4] == 'OP',0].tolist())

#print (df)

