import pandas as pd
#import numpy as np

df = pd.read_excel('AllReview.xlsx',sheet_name = 'Review',index_col=0)

def get_sdx(text):
    text = str(text)
    words_list = text.strip().replace('.','').replace(';','; ').split(' ')
    sdx = [i[:-1] for i in words_list if ':' in i]
    sdx = [''] if len(sdx) == 0 else sdx
    sdx.insert(0,'No') if text.count(':') == text.count(';') else sdx.insert(0,'Yes')
    return sdx

df['s_dx'] = df['Suggested Codes'].apply(get_sdx)

my_dict = dict(zip(df.index, df.s_dx))

my_list = []

for i in my_dict:
	 for l in my_dict[i]:
		 my_list.append([i,l])

sicd = pd.DataFrame(my_list,columns=['ID','S_ICD'])

allicd = sicd

allicd = allicd.rename (columns = {'S_ICD':'All_ICD'})

discrepancy = sicd.groupby(['ID']).head(1)

def get_adx(text):
    text = str(text)
    words_list = text.strip().replace('.','').split(' ')
    adx = [i[:-1] for i in words_list if ';' in i]
    adx = [''] if len(adx) == 0 else adx
    return adx

df['a_dx'] = df['MRA- All Active Codes'].apply(get_adx)

my_dict = dict(zip(df.index, df.a_dx))

my_list = []

for i in my_dict:
	 for l in my_dict[i]:
		 my_list.append([i,l])

aicd = pd.DataFrame(my_list,columns=['ID','A_ICD'])

allicd = allicd.append(pd.DataFrame(my_list,columns=['ID','All_ICD']),ignore_index=True)

icd2d = pd.read_excel('ICD2D.xlsx')

alld = pd.merge (allicd, icd2d, how = 'inner', left_on = 'All_ICD', right_on = 'ICD')

alldd = alld[['ID','Disease']].merge(alld[['ID','Disease']], on='ID')
alldd.drop_duplicates(inplace=True)

icdhcc = pd.read_excel('ICD2HCC2020.xlsx')

hccweights = pd.read_excel('HCC_Weight.xlsx')



icdweights = pd.merge(hccweights, icdhcc, how='inner', right_on = 'CMS-HCC Model Category V24', left_on = 'HCC')

sicdweights = pd.merge(sicd, icdweights, how = 'inner', left_on = 'S_ICD', right_on = 'Diagnosis Code')
sdxweights = sicdweights.groupby(['ID'])['Weight'].sum().reset_index() #else indexing does not happen and hence gives series as output. Need dataframe as output and reindexing will do that.

aicdweights = pd.merge(aicd, icdweights, how = 'inner', left_on = 'A_ICD', right_on = 'Diagnosis Code')
adxweights = aicdweights.groupby(['ID'])['Weight'].sum().reset_index() #else indexing does not happen and hence gives series as output. Need dataframe as output and reindexing will do that.

discrepancy_sdxweights = pd.merge(discrepancy, sdxweights, how='left', left_on = 'ID', right_on='ID')

discrepancy_sdxweights_adxweights = pd.merge(discrepancy_sdxweights, adxweights, how='left', left_on = 'ID', right_on='ID')

discore = pd.read_excel('DI_Score.xlsx', index_col = 0)


output = discrepancy_sdxweights_adxweights

#output.to_excel('AllResult.xlsx',index=True)

print ('Exported')
