#get necessary inputs

#get raw data file name
input_file = input ('give name of medi-cal fee schedule date file with extension: ')

#getting nurse modifier codes count
configurednursemodifiers = int (input ('Give count of configured nurse anesthetist modifier codes: '))

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

c_pos_op_uaub_list = []

while True: #true is never a reason to stop...will go on forever
  new_item = int (input("> "))
  if new_item == 0:
      break#breaks the loop
  else:
      c_pos_op_uaub_list.append (new_item)
  continue #continues the loop/starts over

print("\nInstructions: Of the above list which POS codes are for UAUB In-patient? Enter '0' to stop adding POS codes.")

c_pos_ip_uaub_list = []

while True: #true is never a reason to stop...will go on forever
  new_item = int (input("> "))
  if new_item == 0:
      break#breaks the loop
  else:
      c_pos_ip_uaub_list.append (new_item)
  continue #continues the loop/starts over

c_pos_input = []
c_pos_input.extend ( pos_cutback_input +  c_pos_op_uaub_list + c_pos_ip_uaub_list)
c_pos_input.append (23)

pos_uaub_input = []
pos_uaub_input.extend (c_pos_op_uaub_list + c_pos_ip_uaub_list)

print ('Configured POS codes are: ', c_pos_input)

#pos_op_uaub = int (input ('How many of the total configured POS are for UAUB Out-patient POS? '))

#pos_ip_uaub = int (input ('How many of the total configured POS are for UAUB In-patient POS? '))

#using inputs to find count of inbetween specialty rules for P proctype
total_specialty_rules_p = configuredspecialty_p * 2 + 1 - (subsequentspecialty_p - subsequentspecialtyseries_p) - extremespecialty_p
specialtyinbetween_p = total_specialty_rules_p - configuredspecialty_p

#using inputs to find count of inbetween specialty rules for Q proctype
total_specialty_rules_q = configuredspecialty_q * 2 + 1 - (subsequentspecialty_q - subsequentspecialtyseries_q) - extremespecialty_q
specialtyinbetween_q = total_specialty_rules_q - configuredspecialty_q

#using inputs to find count of inbetween specialty rules for 3 proctype
total_specialty_rules_3 = configuredspecialty_3 * 2 + 1 - (subsequentspecialty_3 - subsequentspecialtyseries_3) - extremespecialty_3
specialtyinbetween_3 = total_specialty_rules_3 - configuredspecialty_3

#creating a parser for fixed width text file. This is the fee schedule raw data file

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
with open (input_file) as fh:
  for line in fh: #accessing each line
    #line = fh.readline()
    # in python 2, print line
    # in python 3
    #print(line)
    
    fields = parse(line)#.rstrip('\n')) # parsing each line. fields to input already given above
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
fh.close()

#print (filedata)

#Using file data to prepare lists based on proc types

iklmn_codes = [x[1] for x in filedata if x[0] in ['I','K','L','M','N']]
p_codes = [x[1] for x in filedata if x[0] == 'P']
q_codes = [x[1] for x in filedata if x[0] == 'Q']
codes_3 = [x[1] for x in filedata if x[0] == '3']

#Using above list to identify duplicate codes list

iklmn_p = [val for val in set(iklmn_codes) if val in set(p_codes)]

iklmn_q = [val for val in set(iklmn_codes) if val in set(q_codes)]

iklmn_3 = [val for val in set(iklmn_codes) if val in set(codes_3)]

#reading uaub file

import pandas #pip install pandas
import numpy

filedata_uaub = pandas.read_csv("feb16_uaub.csv", skiprows=2)

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
    if row.Difference > 0:#codes that are in range
        for i in range (0,int(row.Difference)):
            code = numpy.base_repr(int(row.From,36) + i,36)#alphanumeric counter
            new_list.append([code,code,row.UA,row.UB,row.POS])
    else:#for codes that are not in range
        new_list.append([row.From,row.From,row.UA,row.UB,row.POS])

#making a dataframe out of list of list
df = pandas.DataFrame (new_list)

#identifying codes that require uaub for inpatient and outpatient pos

uaub_ip = set(df.loc[df[4] == 'IP',0].tolist())

uaub_op = set(df.loc[df[4] == 'OP',0].tolist())

#reading every line in the file and find out rules to be inserted

code_dict = {}

prof_fs, prof_efs = 0, 0

for everyline in filedata:
  code_dict.update({everyline[1]:[0,0,0,0]})
for everyline in filedata:
  if everyline[0] not in ['E','F','O','R']:# and everyline[1] == '56420':
    proctype = everyline[0]
    #print (proctype)
    cpt = everyline[1]
    #print ('For ',cpt)
    basicrate = everyline[3]
    childrate = everyline[4]
    errate = everyline[5]
    cutbackind = everyline[7]
    profcomp = everyline[8]
    rentalrate = everyline[9]
    
    #identify correct pos to be used based on er, cutback and uaub requirements

    pos_lista = []

    #removing uaub pos if code does not have uaub rates
    
    if cpt not in uaub_op:
      c_pos_list_a = [pos for pos in c_pos_input if pos not in c_pos_op_uaub_list]
      c_pos_op_uaub = 0
    else:
      c_pos_list_a = c_pos_input
      c_pos_op_uaub = len(c_pos_op_uaub_list)

    #print ('count of configured pos for op uaub ', c_pos_op_uaub)
    
    if cpt not in uaub_ip:
      c_pos_list = [pos for pos in c_pos_list_a if pos not in c_pos_ip_uaub_list]
      c_pos_ip_uaub = 0
    else:
      c_pos_list = c_pos_list_a
      c_pos_ip_uaub = len(c_pos_ip_uaub_list)

    #print ('count of configured pos for ip uaub ', c_pos_op_uaub)

    #print ('configured pos to be used after considering uaub configuration',c_pos_list)

    pos_list = [] #used to ultimately identify inbetween pos
      
    if errate == '--':
      if cutbackind == '0':#no er nor cutback
        pos_list = [pos for pos in c_pos_list if pos in pos_uaub_input]#removed pos that were configured for er and cutback since code does not have those rates. may or may not have added uaub pos
      else:#no er but cutback is present
        pos_list.extend(c_pos_list)
        pos_list.remove(23) #removed only er pos
    else:
      if cutbackind == '0':# er is present but no cutback 
        pos_list.append(23)#added er pos
        pos_list.extend (pos for pos in c_pos_list if pos in pos_uaub_input) # may or may not have added uaub pos
      else:
        pos_list.extend(c_pos_list)#removed nothing
    
    #print (c_pos_list)
    #print ('configured pos to be used after further considering er and cutback configuration ',pos_list)

    #pos_list is the list of pos that must be used to add rates based on configuration of er, cutback and uaub

    possplit = 1 if 1 not in pos_list else 0

    for number in pos_list:
        if number + 1 not in pos_list:
            possplit = possplit + 2
            #print (count)
        else:
            possplit = possplit +1
            #print (count)    

    possplit = possplit - 1 if 99 in pos_list else possplit
    
    inbetween_pos = possplit - len(pos_list) #found count of inbetween pos rules to be added

    #converting list of pos to count 
    configured_pos = 0 if type (pos_list) is None else len(pos_list)
    
    if configured_pos is not 0:
      pos_medi_cal = configured_pos - c_pos_op_uaub #if cpt in uaub_op else configured_pos
      pos_medi_cal = pos_medi_cal - c_pos_ip_uaub #if cpt in uaub_ip else pos_medi_cal
    else:
      pos_medi_cal = 0

    #print ('count of pos for medi-cal only',pos_medi_cal)

    if cpt in iklmn_p and proctype == 'P':
      c_spl = configuredspecialty_p
    elif cpt in iklmn_q and proctype == 'Q':
      c_spl = configuredspecialty_q
    elif cpt in iklmn_3 and proctype == '3':
      c_spl = configuredspecialty_3
    else:
      c_spl = 0

    if proctype in ['I','K','L','M','N']:
      if cpt in iklmn_p:
        ib_spl = specialtyinbetween_p
      if cpt in iklmn_q:
        ib_spl = specialtyinbetween_q
      if cpt in iklmn_3:
        ib_spl = specialtyinbetween_3
      else:
        ib_spl = 1
    else:
      ib_spl = 1

    #print (ib_spl)

    fs = 1 if basicrate not in ['$0.00','$0.01'] else 0

    if fs == 1 and proctype in ['J', 'P', 'Q', '3', 'I', 'K', 'L', 'M', 'N']:
      child_component = (pos_medi_cal * c_spl) + (pos_medi_cal * ib_spl) + (inbetween_pos * c_spl) + (inbetween_pos * ib_spl) if childrate != '---' else 0
      adult_component = (pos_medi_cal * c_spl) + (pos_medi_cal * ib_spl) + (inbetween_pos * c_spl)
      nurse_component = configurednursemodifiers if proctype == 'J' else 0
      uaub_op_component = (c_pos_op_uaub * 2 * c_spl) + (c_pos_op_uaub * 2 * ib_spl) # 2 is the count of modifiers UA and UB.
      uaub_ip_component = (c_pos_ip_uaub * 2 * c_spl) + (c_pos_ip_uaub * 2 * ib_spl) # 2 is the count of modifiers UA and UB.
    else:
      child_component, adult_component, nurse_component, uaub_op_component, uaub_ip_component = 0, 0, 0, 0, 0

    rental_component = 1 if rentalrate != '$0.00' else 0

    efs = child_component + adult_component + nurse_component + uaub_op_component + uaub_ip_component + rental_component

    if profcomp != '0.00':
      prof_fs = 1 if fs == 1 else 0
      prof_efs = 1 if efs != 0 else 0
    else:
      prof_fs, prof_efs = 0, 0

    #print ('identified rules count ', fs, prof_fs, efs, prof_efs)
    #print ('original count ', code_dict.get(cpt))
    cpt_details = numpy.add(code_dict.get(cpt),[fs, prof_fs, efs, prof_efs]).tolist()
    #print ('count after adding ', cpt_details)
    cpt_details[0] = 1 if cpt_details[0] == 2 else cpt_details[0]
    #print ('count after adjusting fs count ', cpt_details)
    code_dict.update({cpt:cpt_details})
    #print ('count after updating dictionary', code_dict.get(cpt))

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

###pip install pyodbc
##import pyodbc 
##cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
##                      "Server=172.16.4.76;"
##                      "Database=CLINICASQA;"
##                      "UID=SA;PWD=Qu1CkMed@2017")
##
##
##cursor = cnxn.cursor()
##cursor.execute('SELECT ClaimNo, * FROM vwClaims WHERE StatementDateFrom <> ServiceFromDate')
##
##for row in cursor.fetchall():
##    print (row[0])
##
##cnxn.close()
       
##        if cpt in pqr_iklmn:
##          cptdetails = list(get_rule_count (basicrate = basic, childrate = child, errate = er, cutbackrate = cutback, profcomp = prof, rentalrate = rental, configured_spl = configuredspecialty, inbetween_spl = specialtyinbetween, nursemodifiers = 0, pos_list = c_pos_list))
##          cptdetails.append ('Multi' if cpt in multi_occurance else 'Single')
##          cptdetails.append ('pqr_iklmn')
##          print ('pqr_iklmn', cpt, cptdetails)
##        elif cpt in g1_pq3iklmn:
##          cptdetails = list(get_rule_count (basicrate = basic, childrate = '---', errate = '--', cutbackrate = 0, profcomp = '0.00', rentalrate = '$0.00', configured_spl = 0, inbetween_spl = 0, nursemodifiers = 0, pos_list = c_pos_list))
##          cptdetails.append ('Multi' if cpt in multi_occurance else 'Single')
##          cptdetails.append ('g1_pq3iklmn')
##          print ('g1_pq3iklmn', cpt, cptdetails)
##        elif proctype == 'J':
##          cptdetails = list(get_rule_count (basicrate = basic, childrate = child, errate = er, cutbackrate = cutback, profcomp = prof, rentalrate = rental, configured_spl = 0, inbetween_spl = 0, nursemodifiers = configurednursemodifiers, pos_list = c_pos_list))
##          cptdetails.append ('Multi' if cpt in multi_occurance else 'Single')
##          cptdetails.append ('Anesthesia')
##          print (cpt, cptdetails)
##        else:
##          cptdetails = list(get_rule_count (basicrate = basic, childrate = child, errate = er, cutbackrate = cutback, profcomp = prof, rentalrate = rental, configured_spl = 0, inbetween_spl = 0, nursemodifiers = 0, pos_list = c_pos_list))
##          cptdetails.append ('Multi' if cpt in multi_occurance else 'Single')
##          cptdetails.append ('All Others')
##          print (cpt, cptdetails)
    #code_dict.update({cpt:cptdetails})

#print (code_dict)
