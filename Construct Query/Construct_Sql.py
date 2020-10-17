list_param = [
    "@Pat_UID",
"@Pat_mobile",
"@Pat_LastName",
"@Pat_FirstName",
"@Pat_MiddleName",
"@Pat_DOB",
"@Pat_PinCode",
"@page_index",
"@page_Size",
"@email",
"@get_count"
]

sql = 'exec {0} '.format('SearchPatient')
p = ''

for param in list_param:
    p = p + param + " = %s, "

p = p[:-1]

print (sql + p)