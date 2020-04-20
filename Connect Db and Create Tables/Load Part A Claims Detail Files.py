import pandas as pd
df = pd.read_fwf('P.A3091.ACO.CCLF2.D180207.T0758041.roff',
                 widths = [13,10,11,2,10,10,4,10,5,11,6,10,10,24,17,2,2,2,2,2],
                 names = ['ClaimID',
                          'LineID',
                          'BeneficiaryHICN',
                          'ClaimType',
                          'LineFromDate',
                          'LineThruDate',
                          'RevenueCode',
                          'RevenueCenterDate',
                          'HCPCS',
                          'HICN_U',
                          'FacilityID',
                          'ClaimFromDate',
                          'ClaimThruDate',
                          'Unit',
                          'Pmt_amt',
                          'Modifier1',
                          'Modifier2',
                          'Modifier3',
                          'Modifier4',
                          'Modifier5'])

df = df.astype(str)

df['LineFromDate'] = pd.to_datetime(df['LineFromDate'], errors = 'coerce')
df['LineThruDate'] = pd.to_datetime(df['LineThruDate'], errors = 'coerce')
df['RevenueCenterDate'] = pd.to_datetime(df['RevenueCenterDate'], errors = 'coerce')
df['ClaimFromDate'] = pd.to_datetime(df['ClaimFromDate'], errors = 'coerce')
df['ClaimThruDate'] = pd.to_datetime(df['ClaimThruDate'], errors = 'coerce')
df['ClaimID'] = pd.to_numeric(df['ClaimID'], errors = 'coerce')
df['LineID'] = pd.to_numeric(df['LineID'], errors = 'coerce')
df['Pmt_amt'] = pd.to_numeric(df['Pmt_amt'], errors = 'coerce')

#print (df['LineFromDate'])

#df[['TOB3','OperatingNPI','AttendingNPI','OtherNPI']] = df[['TOB3','OperatingNPI','AttendingNPI','OtherNPI']].apply(pd.to_numeric, errors = 'coerce')

print (df.dtypes)
print (df.shape)

from sqlalchemy import create_engine
engine = create_engine('mssql+pymssql://sa:12345678@LTP232\sqlexpress/ACO')

print ('engine created')

engine.connect()

print ('engine connected')

df.to_sql(name='AClaimsDetail', con=engine, if_exists='append', index=False)

print ('data appended')
