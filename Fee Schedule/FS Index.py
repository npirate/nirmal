#print ('hello world')

##from openpyxl import load_workbook
##
##wb = load_workbook('rates_data.xls')
##
##ws_input = wb.get_sheet_by_name('rates')
##
##print ('ws_input')

import struct
#import re
#pattern = re.compile("\s{4}\w{3}\s{1}.+")

fieldwidths = (1, -1, 5, -42, 9, -1, 9, -1, 9, -1, 9, -1, 3, -3, 1, -1, 4, -1, 9)  # negative widths represent ignored padding fields
fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's')
                        for fw in fieldwidths)
fieldstruct = struct.Struct(fmtstring)
unpack = fieldstruct.unpack_from
parse = lambda line: tuple(s.decode() for s in unpack(line.encode()))
#print('fmtstring: {!r}, recsize: {} chars'.format(fmtstring, fieldstruct.size))

##line = 'J	00100	ANESTH SALIVARY GLAND                   	     4.52	   $63.33	    ---  	    --   	002	0	0	0.00	    $0.00	Y'
##
##fields = parse(line)
###print('fields: {}'.format(fields))
##print (fields)
##type (fields)
##
##tuple_my = (1, 2)
##print (tuple_my[1])

configurednursemodifiers = int (input ('Give count of configured nurse anesthetist modifier codes: '))

subsequentspecialty = 0
subsequentspecialtyseries = 0
extremespecialty = 0

configuredspecialty = int (input ('Give count of configured specialty codes: '))
if configuredspecialty != 0 and configuredspecialty != 1:
    subsequentspecialty = int (input ('Give count of subsequent specialty codes: '))
    subsequentspecialtyseries = int (input ('Give count of series of subsequent specialty codes: '))
if configuredspecialty != 0:
    extremespecialty = int (input ('Extreme specialty codes? (0 / 1 / 2): '))
#if extremespecialty != 0:
#    extremeinseries = input ('How many extreme codes are part of series of subsequent specialty codes: ')

specialtysplit = configuredspecialty * 2 + 1 - (subsequentspecialty - subsequentspecialtyseries) - extremespecialty
specialtyinbetween = specialtysplit - configuredspecialty
print (specialtysplit)

###erpos = 1
##subsequentpos = 0
##subsequentposseries = 0
##extrementpos = 0
##
##configuredpos = int (input ('Give count of configured pos codes including 23 for ER POS: '))# + erpos
##
##
##if configuredpos != [0,1]:# and configuredpos != 1:
##    subsequentpos = int (input ('Give count of subsequent pos codes: '))
##    subsequentposseries = int (input ('Give count of series of subseqent pos codes: '))
##    pos2324 = int (input ('How many of configured cutback pos codes are 22 or 24 (0 / 1 / 2): '))
##if configuredpos != 0:
##    extremepos = int (input ('Extreme pos codes? (0 / 1 / 2): '))
##possplit = configuredpos * 2 + 1 - (subsequentpos - subsequentposseries) - extrementpos
##posinbetween = possplit - configuredpos
##print (possplit)

pos_list = [] #could also use list() function

print("Enter configured POS codes")
print("Enter '0' to stop adding POS codes.")

while True: #true is never a reason to stop...will go on forever
  new_item=int (input("> "))
  if new_item == 0:
      break#breaks the loop
  else:
      pos_list.append (new_item)
  continue #continues the loop/starts over

print("Here's your list: ",pos_list)

#for item in shopping_list: #don't have to call them "items" - can call them anything - all elements of container, when we get to last item in list, loop stops
 # print(item)

def pos_splitter(errate, cutback):
    if errate != '---':
        if cutback != '---':
            return
        else:
            pos_list.clear()
            pos_list.append(21)
    else:
        if cutback != '---':
            pos_list.remove(21)
        else:
            pos_list.clear()
            
    possplit = 1 if 1 not in pos_list else 0
    #print (count)

    for number in pos_list:
        if number + 1 not in pos_list:
            possplit = possplit + 2
            #print (count)
        else:
            possplit = possplit +1
            #print (count)

    possplit = possplit - 1 if 99 in pos_list else possplit
    inbetweenpos = possplit - len(pos_list)
    return possplit, inbetween

    #print (count)

                            
filedata = []
code_dict = {}
count = 0
# file handle fh
fh = open('rates_data_march.txt')
while True and count < 10:
    # read line
    line = fh.readline()
    # in python 2, print line
    # in python 3
    #print(line)
    fields = parse(line)#.rstrip('\n'))
#print('fields: {}'.format(fields))
#fieldwidths = (1, -1, 5, -42, 9, -1, 9, -1, 9, -1, 9, -1, 3, -3, 1, -1, 4, -1, 9)
    rulecount = [count]
    proctype = fields[0].strip()
    cpt = fields[1].strip()
    unitvalue = fields[2].strip()
    basicrate = fields[3].strip()
    childrate = fields[4].strip()
    errate = fields[5].strip()
    convind = fields[6].strip()
    cutrate = fields[7].strip()
    profcomp = fields[8].strip()
    rentalrate = fields[9].strip()
    filedata.append ([proctype, cpt, unitvalue, basicrate, childrate, errate, convind,  cutrate, profcomp, rentalrate])
    #code_dict.update({cpt:rulecount})
    
    count += 1
    # check if line is not empty
    if not line:
        break
fh.close()
#print (code_dict)
print (filedata)

#firstlist = ['I','K','L','M','N']
#secondlist = ['P','Q','3']
firstlist = [x[1] for x in filedata if x[0] in ['I','K','L','M','N','J']]
secondlist = [x[1] for x in filedata if x[0] in ['P','Q','3','J']]
pq3_iklmn = [val for val in set(firstlist) if val in set(secondlist)]

allcodes = [x[1] for x in filedata]
allcodes.append('00100')

def FindMultipleOccurance(L):
    seen = set()
    seen2 = set()
    seen_add = seen.add
    seen2_add = seen2.add
    for item in L:
        if item in seen:
            seen2_add(item)
        else:
            seen_add(item)
    return list(seen2)

multi_occurance = FindMultipleOccurance(L = allcodes)
print (multi_occurance)

def update_prof (fs, efs, profcomp):
    if profcomp != '0.00':
        prof_fs = 'Y' if fs > 0 else 'N'
        prof_efs = 'Y' if efs > 0 else 'N'
    else:
        prof_fs, prof_efs = 'N'
    return prof_fs, prof_efs

def get_rule_count (basicrate, childrate, errate, cutrate, profcomp, rentalrate, configured_a, configured_b, inbetween_b):
    fs = 1 if basicrate != '$0.00' else 0

    if childrate != '---':
        child_component = (configured_a * configured_b) + (configured_a * inbetween_b) + (inbetween_a * configured_b) + (inbetween_a * inbetween_b)
    else:
        child_component = 0

    configured_a, inbetween_a = pos_splitter (errate, cutback)

    adult_component = (configured_a * configured_b) + (configured_a * inbetween_b) + (inbetween_a * configured_b)

    rental_component = 1 if rentalrate != '$0.00' else 0

    efs = child_component + adult_component + rental_component

    total = fs + efs

    update_prof (fs, efs, profcomp)

    return total

fsrc = 0
prof_fs = 'N'
efsrc = 0
prof_efs = 'N'
bucket = None

for everyline in filedata:
    if everyline[1] not in code_dict:
        proctype = everyline[0]
        cpt = everyline[1]
        basicrate = everyline[3]
        childrate = everyline[4]
        errate = everyline[5]
        cutrate = everyline[7]
        profcomp = everyline[8]
        rentalrate = everyline[9]
        if proctype == 'J':
            fsrc = 1 if basicrate != '$0.00' else 'N'
            #prof_fs = 'Y' if profcomp != '0.00' and fsrc = 1 else 'N'
            efsrc = configurednursemodifiers
            prof_efs == 'Y' if profcomp != '0.00' and efsrc != 0 else 'N'
            #bucket = 'Anesthesia'
            occurance = 'Multi' if cpt in multi_occurance else 'Single'
            duplicate = 'Y' if cpt in pq3_iklmn else 'N'
            total = fsrc + efsrc
            print (cpt, total, fsrc, prof_fs, efsrc, prof_efs, occurance, duplicate)
        #elseif everyline[0] not in ['E','F','O','R','G','1') and everyline[1] not in pq3_iklmn:
            fsrc = 1 if basicrate != '$0.00' else 'N'
            #prof_fs = 'Y' if profcomp != '0.00' and fsrc = 1 else 'N'
            

            #efsrc = 
  


list1 = [['1','2'],['1','2']]
#import collections
#print [item for item, count in collections.Counter(list1).items() if count > 1
dupes = [x for n, x in enumerate(list1) if x in list1[:n]]
print (dupes)
