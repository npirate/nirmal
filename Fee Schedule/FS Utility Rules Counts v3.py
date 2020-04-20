#creating a parser for fixed width text file.

from itertools import zip_longest as izip_longest
from itertools import accumulate

def parser (fieldwidths):
  cuts = tuple(cut for cut in accumulate(abs(fw) for fw in fieldwidths))
  pads = tuple(fw < 0 for fw in fieldwidths) # bool values for padding fields
  flds = tuple(izip_longest(pads, (0,)+cuts, cuts))[:-1]  # ignore final one
  parse = lambda line: tuple(line[i:j] for pad, i, j in flds if not pad)
  # optional informational function attributes
  parse.size = sum(abs(fw) for fw in fieldwidths)
  parse.fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's')
                        for fw in fieldwidths)
  return parse

#define widths that should be and shouldnt be parsed
fieldwidths = (1, -1, 5, -42, 9, -1, 9, -1, 9, -1, 9, -1, 3, -3, 1, -1, 4, -1, 9)  # negative widths represent ignored padding fields

#parsed details would go to the object
parse = parser(fieldwidths)

#using the parser to read the file's individual line and put individual line's parsed fields to a list.

#Hence creating blank list that will hold each line's data

filedata = []

#opening txt file
with open (input ('Give name of medi-cal fee schedule date file with extension: ')) as file:
  for each_line in file: #accessing each line
    #line = fh.readline()
    # in python 2, print line
    # in python 3
    #print(line)
    
    fields = parse(each_line)#.rstrip('\n')) # parsing each line. fields to input already given above
##    proctype = fields[0].strip()
##    cpt = fields[1].strip()
##    unitvalue = fields[2].strip()
##    basicrate = fields[3].strip()
##    childrate = fields[4].strip()
##    errate = fields[5].strip()
##    convind = int (fields[6].strip())
##    cutrate = fields[7].strip()
##    profcomp = fields[8].strip()
##    rentalrate = fields[9].strip()

    #if fields[1].strip() == '27792':
    filedata.append ([fields[0].strip(), fields[1].strip(), fields[2].strip(), fields[3].strip(), fields[4].strip(), fields[5].strip(), int (fields[6].strip()), fields[7].strip(), fields[8].strip(), fields[9].strip()])
       
    #count += 1
    # check if line is not empty
    #if not line:
        #break
file.close()

print('File has been read.')

#get necessary inputs

#getting nurse modifier codes count
nurse_modifiers_count = int (input ('Give count of configured nurse anesthetist modifier codes: '))

#storing specialty configuration

spl_conf = {}

#getting specialty codes configured for P proc type
subsequentspecialty_p, subsequentspecialtyseries_p, extremespecialty_p = 0, 0, 0
configuredspecialty_p = int (input ('Give count of configured specialty codes for P proc type: '))
if configuredspecialty_p not in [0,1]:
  print ('\nInstructions: A B H I J means subsequent specialty codes are 5 and series of subsequent specialty codes are 2\n')
  subsequentspecialty_p = int (input ('Give count of subsequent specialty codes: '))
  subsequentspecialtyseries_p = int (input ('Give count of series of subsequent specialty codes: '))
if configuredspecialty_p != 0:
  print ('\nInstructions: In list of master codes A to Z, A and Z are extrement specialty codes\n')
  extremespecialty_p = int (input ('Give count of extreme specialty codes? (0 / 1 / 2): '))

#using inputs to find count of inbetween specialty rules for P proctype
total_specialty_rules_p = configuredspecialty_p * 2 + 1 - (subsequentspecialty_p - subsequentspecialtyseries_p) - extremespecialty_p
specialtyinbetween_p = total_specialty_rules_p - configuredspecialty_p

spl_conf['P'] = [configuredspecialty_p,specialtyinbetween_p]

#getting specialty codes configured for Q proc type
subsequentspecialty_q, subsequentspecialtyseries_q, extremespecialty_q = 0, 0, 0
configuredspecialty_q = int (input ('Give count of configured specialty codes for Q proc type: '))
if configuredspecialty_q not in [0,1]:
  print ('\nInstructions: A B H I J means subsequent specialty codes are 5 and series of subsequent specialty codes are 2\n')
  subsequentspecialty_q = int (input ('Give count of subsequent specialty codes: '))
  subsequentspecialtyseries_q = int (input ('Give count of series of subsequent specialty codes: '))
if configuredspecialty_q != 0:
  print ('\nInstructions: In list of master codes A to Z, A and Z are extrement specialty codes\n')
  extremespecialty_q = int (input ('Give count of extreme specialty codes? (0 / 1 / 2): '))

#using inputs to find count of inbetween specialty rules for Q proctype
total_specialty_rules_q = configuredspecialty_q * 2 + 1 - (subsequentspecialty_q - subsequentspecialtyseries_q) - extremespecialty_q
specialtyinbetween_q = total_specialty_rules_q - configuredspecialty_q

spl_conf['Q'] = [configuredspecialty_q,specialtyinbetween_q]

#getting specialty codes configured for 3 proc type
subsequentspecialty_3, subsequentspecialtyseries_3, extremespecialty_3 = 0, 0, 0
configuredspecialty_3 = int (input ('Give count of configured specialty codes for 3 proc type: '))
if configuredspecialty_3 not in [0,1]:
  print ('\nInstructions: A B H I J means subsequent specialty codes are 5 and series of subsequent specialty codes are 2\n')
  subsequentspecialty_3 = int (input ('Give count of subsequent specialty codes: '))
  subsequentspecialtyseries_3 = int (input ('Give count of series of subsequent specialty codes: '))
if configuredspecialty_3 != 0:
  print ('\nInstructions: In list of master codes A to Z, A and Z are extrement specialty codes\n')
  extremespecialty_3 = int (input ('Give count of extreme specialty codes? (0 / 1 / 2): '))

#using inputs to find count of inbetween specialty rules for 3 proctype
total_specialty_rules_3 = configuredspecialty_3 * 2 + 1 - (subsequentspecialty_3 - subsequentspecialtyseries_3) - extremespecialty_3
specialtyinbetween_3 = total_specialty_rules_3 - configuredspecialty_3

spl_conf['3'] = [configuredspecialty_3,specialtyinbetween_3]

#getting configured pos

print("\nInstructions: Enter all configured POS codes for Cutback Rates. Enter '0' to stop adding POS codes.")

pos_cutback_input = []

while True: #true is never a reason to stop...will go on forever
  new_item = int (input("> "))
  if new_item == 0:
      break#breaks the loop
  else:
      pos_cutback_input.append (new_item)
  continue #continues the loop/starts over

print("\nInstructions: Of the above list which POS codes are for UAUB Out-patient? Enter '0' to stop adding POS codes.")

pos_op_uaub_input = []

while True: #true is never a reason to stop...will go on forever
  new_item = int (input("> "))
  if new_item == 0:
      break#breaks the loop
  else:
      pos_op_uaub_input.append (new_item)
  continue #continues the loop/starts over

print("\nInstructions: Of the above list which POS codes are for UAUB In-patient? Enter '0' to stop adding POS codes.")

pos_ip_uaub_input = []

while True: #true is never a reason to stop...will go on forever
  new_item = int (input("> "))
  if new_item == 0:
      break#breaks the loop
  else:
      pos_ip_uaub_input.append (new_item)
  continue #continues the loop/starts over

all_pos_input = []
all_pos_input.extend (pos_cutback_input +  pos_op_uaub_input + pos_ip_uaub_input)
all_pos_input.append (23)

print ('Configured POS codes are: ', all_pos_input)

#read uauab data

import pandas #pip install pandas
import numpy

filedata_uaub = pandas.read_csv("jan16_uaub.csv", skiprows=2)

#separating out outpatient rates
outpatient_df = filedata_uaub[['From','Thru','UA','UB']]
outpatient_df['POS'] = 'OP'

#separating out inpatient rates
inpatient_df = filedata_uaub[['From.1','Thru.1','UA.1','UB.1']]
inpatient_df.columns = ['From','Thru','UA','UB']
inpatient_df['POS'] = 'IP'

#merging the two rates in single object / dataframe
df = pandas.concat([outpatient_df, inpatient_df],ignore_index = True)

#identifying codes which are in range
df['Difference'] = numpy.where(df['From'] == df['Thru'],0,df['Thru'].str[1:].apply(pandas.to_numeric) - df['From'].str[1:].apply(pandas.to_numeric)+1)

#converting range to individual codes by incrementing through a range
new_list = []

for row in df.itertuples():
    if row.Difference > 0:# and row.From == '68801':#codes that are in range
        #print (row.Difference)
        for i in range (0,int(row.Difference)):
            code = numpy.base_repr(int(row.From[1:],10) + int(i),10)#alphanumeric counter. base 10 is our normal numbers.
            #print (row.From[0:1]+code)
            new_list.append([row.From[0:1]+code,row.From[0:1]+code,row.UA,row.UB,row.POS])
    else:#for codes that are not in range
        new_list.append([row.From,row.From,row.UA,row.UB,row.POS])

#making a dataframe out of list of list
df = pandas.DataFrame (new_list)

#identifying codes that require uaub for inpatient and outpatient pos

uaub_ip_codes = set(df.loc[df[4] == 'IP',0].tolist())

uaub_op_codes = set(df.loc[df[4] == 'OP',0].tolist())

#using medi-cal file data to prepare single occurance and multi-occurance lists

dummy_list = []
multi_occurance_codes = []

for x in filedata:
  if x[1] not in dummy_list:
    dummy_list.append(x[1])
  else:
    multi_occurance_codes.append(x[1])

single_occurance_codes = set(dummy_list) - set(multi_occurance_codes)

##if configuredspecialty_p == 0:
##  proc_type_do_not_load.append('P')
##
##if configuredspecialty_q == 0:
##  proc_type_do_not_load.append('Q')
##
##if configuredspecialty_3 == 0:
##  proc_type_do_not_load.append('3')

#Using medi-cal file data to prepare lists based on proc types

iklmn_codes = [x[1] for x in filedata if x[0] in ['I','K','L','M','N'] and x[3] not in ['$0.00','$0.01']]
pq3_codes = [x[1] for x in filedata if x[0] in ['P','Q','3'] and x[3] not in ['$0.00','$0.01']]
p_codes = [x[1] for x in filedata if x[0] == 'P' and x[3] not in ['$0.00','$0.01']]
q_codes = [x[1] for x in filedata if x[0] == 'Q' and x[3] not in ['$0.00','$0.01']]
codes_3 = [x[1] for x in filedata if x[0] == '3' and x[3] not in ['$0.00','$0.01']]
codes_1 = [x[1] for x in filedata if x[0] == '1' and x[3] not in ['$0.00','$0.01']]

#Using above list to identify duplicate codes list

iklmn_pq3 = [val for val in set(iklmn_codes) if val in set(pq3_codes)]
iklmn_p = [val for val in set(iklmn_codes) if val in set(p_codes)]
iklmn_q = [val for val in set(iklmn_codes) if val in set(q_codes)]
iklmn_3 = [val for val in set(iklmn_codes) if val in set(codes_3)]
 

#identify proc_type that must not be loaded

proc_type_do_not_load = ['E','F','O','R']

#reading every line in the file and find out rules to be inserted

code_dict = {}
fs, prof_fs, efs, prof_efs = 0, 0, 0, 0

for everyline in filedata:
  code_dict.update({everyline[1]:[0,0,0,0]})

for everyline in filedata:
  fs, prof_fs, efs, prof_efs = 0, 0, 0, 0
  if everyline[0] not in proc_type_do_not_load:# and everyline[1] in ['90962', 'X3900','99056']:
    proctype = everyline[0]
    #print (proctype)
    cpt = everyline[1]
    #print ('For: ',proctype,' - ', cpt)
    basicrate = everyline[3]
    childrate = everyline[4]
    #print ('childrate is ',childrate)
    errate = everyline[5]
    cutbackind = everyline[7]
    profcomp = everyline[8]
    rentalrate = everyline[9]

    #identify applicable pos to be used based on er, cutback and uaub requirements

    applicable_pos = []

    if errate == '--':
        if cutbackind == '0': #no er nor cutback
            applicable_pos = []
        else:#no er but cutback is present
            applicable_pos.extend (pos_cutback_input)
    else:
        if cutbackind == '0':# er is present but no cutback
            applicable_pos.append(23) #added er pos
        else:#both er and cutback
            applicable_pos.extend (pos_cutback_input)#added cutback
            applicable_pos.append(23)#added er pos

    applicable_pos.extend (pos_op_uaub_input * 2) if cpt in uaub_op_codes else applicable_pos #2 because rules for two modifiers ua and ub must be added

    applicable_pos.extend (pos_ip_uaub_input * 2) if cpt in uaub_ip_codes else applicable_pos #2 because rules for two modifiers ua and ub must be added

    #print ('applicable pos ', applicable_pos)

    possplit = 1 if 1 not in set(applicable_pos) else 0

    for number in set(applicable_pos):
        if number + 1 not in applicable_pos:
            possplit = possplit + 2
            #print (count)
        else:
            possplit = possplit +1
            #print (count)    

    possplit = possplit - 1 if 99 in set(applicable_pos) else possplit
    
    inbn_pos = 1 if childrate != '---' and (cpt in uaub_ip_codes or cpt in uaub_op_codes) else possplit - len(set(applicable_pos)) #found count of inbetween pos rules to be added

    #print ('inbetween pos ',inbn_pos)

    efs = +1 if rentalrate != '$0.00' else efs

    if basicrate not in ['$0.00','$0.01']:
        if proctype == 'J':
            efs = nurse_modifiers_count
            fs = +1
            #print ('J code fs and efs count ',fs, ' ', efs)
        elif cpt in iklmn_pq3:# and proctype in ['P','Q','3','I','K','L','M','N']:#this is non-J multi occurance but only when p/q/3 is duplicate with i/k/l/m/n. The other duplicate pairs are not considered here.
            if proctype in ['P','Q','3']:
                a = spl_conf[proctype][0] * (len(applicable_pos)+ inbn_pos)
                c = a if childrate != '---' else 0
                efs = efs + a + c
            elif cpt in iklmn_p:
                fs = +1
                a = len(applicable_pos) * spl_conf['P'][1]
                c = a + (inbn_pos * spl_conf['P'][1]) if childrate != '---' else 0
                efs = efs + a + c
            elif cpt in iklmn_q:
                fs = +1
                a = len(applicable_pos) * spl_conf['Q'][1]
                c = a + (inbn_pos * spl_conf['Q'][1]) if childrate != '---' else 0
                efs = efs + a + c
            elif cpt in iklmn_3:
                fs = +1
                a = len(applicable_pos) * spl_conf['3'][1]
                c = a + (inbn_pos * spl_conf['3'][1]) if childrate != '---' else 0
                efs = efs + a + c
            #print ('iklmn_pq3 fs and efs count ',fs, ' ', efs)
        elif (proctype == 'P' and configuredspecialty_p == 0) or (proctype == 'Q' and configuredspecialty_q == 0) or (proctype == '3' and configuredspecialty_3 == 0):
            fs = +1
            a = len(applicable_pos) 
            c = a + inbn_pos if childrate != '---' else 0
            efs = a + c
            #print ('p/q/3 is treated as non-J single occurance due to lack of configuration fs count = {} and efs count = {}'.format(fs,efs))            
        elif cpt in single_occurance_codes:#not based on configuration
            if childrate != '---' and errate == '--' and cutbackind == '0':
                fs = +1
                a = len(applicable_pos)
                c = 1
                efs = a + c
                #print ('non-J single occurance 100 bucket fs count = {} and efs count = {}'.format(fs,efs))
            else:
                fs = +1
                a = len(applicable_pos) 
                c = a + inbn_pos if childrate != '---' else 0
                efs = efs + a + c
                #print ('non-J single occurance fs count = {} and efs count = {}'.format(fs,efs))              
        else:
            if proctype not in ['1','G','P','Q','3']:
                fs = +1
                a = len(applicable_pos) 
                c = a + inbn_pos if childrate != '---' else 0
                efs = efs + a + c
                #print ('non iklmn_pq3 and non 1, G, P, Q, 3 proc_type fs and efs count ',fs, ' ', efs)                
            else:
                fs = +1
                #print ('non iklmn_pq3 and 1, G OR P, Q, 3 but specialty code not configured codes proc_type fs and efs count ',fs, ' ', efs)


        if profcomp != '0.00':
          prof_fs = 1 if fs > 0 else 0
          prof_efs = 1 if efs > 0 else 0
        else:
          prof_fs, prof_efs = 0, 0
          
    else:
      prof_fs, prof_efs = 0, 0

    cpt_details = numpy.add(code_dict.get(cpt),[fs, prof_fs, efs, prof_efs]).tolist()

    cpt_details[0] = 1 if cpt_details[0] == 2 else cpt_details[0]

    cpt_details[1] = 1 if cpt_details[1] == 2 else cpt_details[1]

    cpt_details[3] = 1 if cpt_details[3] == 2 else cpt_details[3]

    #print (cpt_details)

    code_dict.update({cpt:cpt_details})

import csv
##with open('rules_count.csv', 'wb') as csv_file:
##    writer = csv.writer(csv_file)
##    for key, value in code_dict.items():
##       writer.writerow([key, value])

with open('rules_count.csv', 'w') as f:
    [f.write('Code,FS_Rules,FS_Prof_Tech_Component,EFS_Rules,EFS_Prof_Tech_Component\n')]
    [f.write('{0},{1}\n'.format(key, ','.join(map(str,value)))) for key, value in code_dict.items()]

f.close()

print ('Output csv file by name rules_count has been exported successfully')

#### pip install pysftp
##import pysftp
##cnopts = pysftp.CnOpts()
##cnopts.hostkeys = None
##print ('hostkeys set as none')
###with pysftp.Connection('207.178.145.106', username='medvision', password='M3dv1sion', cnopts = cnopts, port = 2222, log = 'log_file.log') as sftp:#clinicas
##with pysftp.Connection('65.74.189.71', username='quickqa', password='99$inmedi', cnopts = cnopts, log = 'log_file.log') as sftp:#India QA
##    print ('sftp connected')
##    try:
##        sftp.chdir('FS_Utility_QA')
##    except:
##        sftp.mkdir('FS_Utility_QA')
##        sftp.chdir('FS_Utility_QA')
##    #with sftp.cd('public'):        # temporarily chdir to public
##     #   print ('test directory created')
##    sftp.put('rules_count.csv')  # upload file to current working remote directory
##        #sftp.get('remote_file')         # get a remote file
##
##print ('File placed on sftp successfully')

