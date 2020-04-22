import pandas as pd

df = pd.read_excel('AllReview.xlsx',sheet_name = 'Review',index_col=0)#using MemberID as index

def get_sdx(text): #function to check if there is discrepancy in count of colon and semicolon in the text and also extract suggested diagnosis codes after removing is dot.
    text = str(text)
    words_list = text.strip().replace('.','').replace(';','; ').split(' ')
    sdx = [i[:-1] for i in words_list if ':' in i]
    sdx = [''] if len(sdx) == 0 else sdx
    sdx.insert(0,'No') if text.count(':') == text.count(';') else sdx.insert(0,'Yes')
    return sdx

df['s_dx'] = df['Suggested Codes'].apply(get_sdx) #applying function and creating new column with the output

my_dict = dict(zip(df.index, df.s_dx)) #adding discrepacy value and suggested diagnosis to dictionary where MemberID is the key

#unravelling dict {key:[value1, value2]} into simple list containing list of two values [[key,value1],[key,value2]]
my_list = []

for i in my_dict:
	 for l in my_dict[i]:
		 my_list.append([i,l])

#making df out of list. MemberID is a seperate column now and not an index anymore.
		 
sicd = pd.DataFrame(my_list,columns=['ID','S_ICD'])


#making a special df containing MemberID and Discrepancy

discrepancy = sicd.groupby(['ID']).head(1)

#function to get captured diagnosis codes for each MemberId. Here we are not capturing any discrepancy

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

#need list of all diagnosis codes to check disease interaction

#copied suggested diagnosis codes

allicd = sicd

allicd = allicd.rename(columns = {'S_ICD':'All_ICD'})

allicd = allicd.append(pd.DataFrame(my_list,columns=['ID','All_ICD']),ignore_index=True) #appended actual diagnosis codes. Ignoring index allowed to append as rows otherwise it was adding a new column of captured diagnosis codes

icd2d = pd.read_excel('ICD2D.xlsx')#reading file that maps icds to disease category

alld = pd.merge (allicd, icd2d, how = 'inner', left_on = 'All_ICD', right_on = 'ICD')

#making a cartesian product of disease categories for a memberid

alldd = alld[['ID','Disease']].merge(alld[['ID','Disease']], on='ID')
alldd.drop_duplicates(inplace=True)

#getting weights for each icd
icdhcc = pd.read_excel('ICD2HCC2020.xlsx')

hccweights = pd.read_excel('HCC_Weight.xlsx')

icdweights = pd.merge(hccweights, icdhcc, how='inner', right_on = 'CMS-HCC Model Category V24', left_on = 'HCC')

#getting weights of suggested icd codes for each memberid
sicdweights = pd.merge(sicd, icdweights, how = 'inner', left_on = 'S_ICD', right_on = 'Diagnosis Code')
sdxweights = sicdweights.groupby(['ID'])['Weight'].sum().reset_index() #else indexing does not happen and hence gives series as output. Need dataframe as output and reindexing will do that.

#getting weights of captured icd codes for each memberid
aicdweights = pd.merge(aicd, icdweights, how = 'inner', left_on = 'A_ICD', right_on = 'Diagnosis Code')
adxweights = aicdweights.groupby(['ID'])['Weight'].sum().reset_index() #else indexing does not happen and hence gives series as output. Need dataframe as output and reindexing will do that.

#getting weights of disease interactions for each memberid
discore = pd.read_excel('DI_Score.xlsx', index_col = 0)

discore = pd.merge(alldd, discore, how='inner', left_on =['Disease_x','Disease_y'], right_on =['DI1','DI2'])
diweights = discore.groupby(['ID'])['Score'].sum().reset_index()

#bringing all weights together for export and hence left join

discrepancy_sdxweights = pd.merge(discrepancy, sdxweights, how='left', left_on = 'ID', right_on='ID')

discrepancy_sdxweights_adxweights = pd.merge(discrepancy_sdxweights, adxweights, how='left', left_on = 'ID', right_on='ID')

discrepancy_sdxweights_adxweights_diweights = pd.merge(discrepancy_sdxweights_adxweights, diweights, how='left', left_on ='ID', right_on='ID')

output = discrepancy_sdxweights_adxweights_diweights

output.to_excel('AllResult.xlsx',index=False)

print ('Exported')
