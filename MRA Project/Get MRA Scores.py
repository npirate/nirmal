import pandas as pd

df = pd.read_excel('MRA Project\Aegis.xlsx',sheet_name = 'Review',index_col=0)#using MemberID as index

#function to check if there is discrepancy in count of colon and semicolon in the text and also extract suggested diagnosis codes after removing is dot.
def get_sdx(text): 
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

discrepancy = discrepancy.rename(columns = {'S_ICD':'Discrepancy?'})

#function to get all active diagnosis codes for each MemberId. Here we are not capturing any discrepancy

def get_adx(text):
    text = str(text)
    words_list = text.strip().replace('.','').split(' ')
    adx = [i[:-1] for i in words_list if ';' in i]
    adx = [''] if len(adx) == 0 else adx
    return adx

df['a_dx'] = df['MRA- All Active Codes'].apply(get_adx)

#function to get all inactive active diagnosis codes for each MemberId. Here we are not capturing any discrepancy


def get_iadx(text):
    text = str(text)
    words_list = text.strip().replace('.','').split(' ')
    iadx = [i[:-1] for i in words_list if ':' in i]
    iadx = [''] if len(iadx) == 0 else iadx
    return iadx

df['ia_dx'] = df['MRA- No Longer Pertains'].apply(get_iadx)

#function to remove ia_dx codes from a_dx

def remove_dx(a_dx, ia_dx):
    res = [i for i in a_dx if i not in ia_dx]
    return res

df['final_active_dx'] = df.apply(lambda x: remove_dx(x.a_dx, x.ia_dx), axis = 1)

my_dict = dict(zip(df.index, df.final_active_dx))

my_list = []

for i in my_dict:
	 for l in my_dict[i]:
		 my_list.append([i,l])

aicd = pd.DataFrame(my_list,columns=['ID','A_ICD'])

#need list of all diagnosis codes - final active and suggested to check disease interaction

#copied suggested diagnosis codes

allicd = sicd

allicd = allicd.rename(columns = {'S_ICD':'All_ICD'})

allicd = allicd.append(pd.DataFrame(my_list,columns=['ID','All_ICD']),ignore_index=True) #appended final active diagnosis codes. Ignoring index allowed to append as rows otherwise it was adding a new column of captured diagnosis codes

icd2d = pd.read_excel('MRA Project\ICD2D.xlsx')#reading file that maps icds to disease category

alld = pd.merge (allicd, icd2d, how = 'inner', left_on = 'All_ICD', right_on = 'ICD')

#making a cartesian product of disease categories for a memberid

alldd = alld[['ID','Disease']].merge(alld[['ID','Disease']], on='ID')
alldd.drop_duplicates(inplace=True)

#getting weights for each icd
icdhcc = pd.read_excel('MRA Project\ICD2HCC2020.xlsx')

hccweights = pd.read_excel('MRA Project\HCC_Weight.xlsx')

icdweights = pd.merge(hccweights, icdhcc, how='inner', right_on = 'CMS-HCC Model Category V24', left_on = 'HCC')

#getting weights of suggested icd codes for each memberid
sicdweights = pd.merge(sicd, icdweights, how = 'inner', left_on = 'S_ICD', right_on = 'Diagnosis Code')
sdxweights = sicdweights.groupby(['ID'])['Weight'].sum().reset_index() #else indexing does not happen and hence gives series as output. Need dataframe as output and reindexing will do that.
sdxweights = sdxweights.rename(columns = {'Weight':'P_MRA_SDx'})

#getting weights of captured icd codes for each memberid
aicdweights = pd.merge(aicd, icdweights, how = 'inner', left_on = 'A_ICD', right_on = 'Diagnosis Code')
adxweights = aicdweights.groupby(['ID'])['Weight'].sum().reset_index() #else indexing does not happen and hence gives series as output. Need dataframe as output and reindexing will do that.
adxweights = adxweights.rename(columns = {'Weight':'P_MRA_ADx'})

#getting weights of disease interactions for each memberid
discore = pd.read_excel('MRA Project\DI_Score.xlsx', index_col = 0)

discore = pd.merge(alldd, discore, how='inner', left_on =['Disease_x','Disease_y'], right_on =['DI1','DI2'])
diweights = discore.groupby(['ID'])['Score'].sum().reset_index()

diweights = diweights.rename(columns = {'Score':'P_MRA_DxInt'})

#bringing all weights together for export and hence left join

discrepancy_sdxweights = pd.merge(discrepancy, sdxweights, how='left', left_on = 'ID', right_on='ID')

discrepancy_sdxweights_adxweights = pd.merge(discrepancy_sdxweights, adxweights, how='left', left_on = 'ID', right_on='ID')

discrepancy_sdxweights_adxweights_diweights = pd.merge(discrepancy_sdxweights_adxweights, diweights, how='left', left_on ='ID', right_on='ID')

output = pd.merge(df, discrepancy_sdxweights_adxweights_diweights, how = 'left', left_index = True, right_on = 'ID')

output = output.drop(['s_dx','a_dx','ia_dx','final_active_dx'], axis = 1)

output.to_excel('MRA Project\AllResult.xlsx',index=False)

print ('Exported')
