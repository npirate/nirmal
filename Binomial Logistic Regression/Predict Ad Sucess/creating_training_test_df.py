Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> pd.read_csv('encoded.csv', index_col = [0])
       runtime            ...             money_back_guarantee_Yes
id                        ...                                     
19717       45            ...                                    0
31593       45            ...                                    0
5681        45            ...                                    1
15491       40            ...                                    0
23587       48            ...                                    0
28523       40            ...                                    1
12290       50            ...                                    0
20866       40            ...                                    1
21312       40            ...                                    0
16479       35            ...                                    0
9875        20            ...                                    0
23314       25            ...                                    0
9457        72            ...                                    1
6387        48            ...                                    0
10499       35            ...                                    0
27353       40            ...                                    0
52          40            ...                                    1
5380        56            ...                                    0
7209        40            ...                                    1
7660        45            ...                                    0
26880       50            ...                                    0
10217       60            ...                                    0
12594       25            ...                                    0
17290       35            ...                                    1
29820       20            ...                                    1
28656       40            ...                                    0
23030       40            ...                                    1
5834        50            ...                                    1
10943       45            ...                                    1
12404       24            ...                                    1
...        ...            ...                                  ...
13516       65            ...                                    0
13986       13            ...                                    1
20293       40            ...                                    1
30938       50            ...                                    0
21575       25            ...                                    0
2005        40            ...                                    1
2227        40            ...                                    1
32186       60            ...                                    0
10817       16            ...                                    1
13093       44            ...                                    0
10397       40            ...                                    0
14055       40            ...                                    0
19374       40            ...                                    0
23099       40            ...                                    1
30927       40            ...                                    1
9543        24            ...                                    1
679         40            ...                                    1
22422        6            ...                                    0
26704       40            ...                                    0
28446       40            ...                                    1
17934       40            ...                                    1
9921        40            ...                                    1
28684       40            ...                                    1
1933        40            ...                                    1
10827       45            ...                                    0
16009       50            ...                                    0
17241       40            ...                                    0
2295        25            ...                                    0
17902       48            ...                                    1
30877       40            ...                                    1

[26048 rows x 73 columns]
>>> df.describe
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    df.describe
NameError: name 'df' is not defined
>>> df = pd.read_csv('encoded.csv', index_col = [0])
>>> df.describe
<bound method NDFrame.describe of        runtime            ...             money_back_guarantee_Yes
id                        ...                                     
19717       45            ...                                    0
31593       45            ...                                    0
5681        45            ...                                    1
15491       40            ...                                    0
23587       48            ...                                    0
28523       40            ...                                    1
12290       50            ...                                    0
20866       40            ...                                    1
21312       40            ...                                    0
16479       35            ...                                    0
9875        20            ...                                    0
23314       25            ...                                    0
9457        72            ...                                    1
6387        48            ...                                    0
10499       35            ...                                    0
27353       40            ...                                    0
52          40            ...                                    1
5380        56            ...                                    0
7209        40            ...                                    1
7660        45            ...                                    0
26880       50            ...                                    0
10217       60            ...                                    0
12594       25            ...                                    0
17290       35            ...                                    1
29820       20            ...                                    1
28656       40            ...                                    0
23030       40            ...                                    1
5834        50            ...                                    1
10943       45            ...                                    1
12404       24            ...                                    1
...        ...            ...                                  ...
13516       65            ...                                    0
13986       13            ...                                    1
20293       40            ...                                    1
30938       50            ...                                    0
21575       25            ...                                    0
2005        40            ...                                    1
2227        40            ...                                    1
32186       60            ...                                    0
10817       16            ...                                    1
13093       44            ...                                    0
10397       40            ...                                    0
14055       40            ...                                    0
19374       40            ...                                    0
23099       40            ...                                    1
30927       40            ...                                    1
9543        24            ...                                    1
679         40            ...                                    1
22422        6            ...                                    0
26704       40            ...                                    0
28446       40            ...                                    1
17934       40            ...                                    1
9921        40            ...                                    1
28684       40            ...                                    1
1933        40            ...                                    1
10827       45            ...                                    0
16009       50            ...                                    0
17241       40            ...                                    0
2295        25            ...                                    0
17902       48            ...                                    1
30877       40            ...                                    1

[26048 rows x 73 columns]>
>>> traine = df.sample(frac=0.8,random_state = 1)
>>> teste = df.drop(traine.index).sample(frac=1.0)
>>> traine.count()
runtime                                   20838
ratings                                   20838
netgain                                   20838
relationship_Divorced                     20838
relationship_Married-AF-spouse            20838
relationship_Married-civ-spouse           20838
relationship_Married-spouse-absent        20838
relationship_Never-married                20838
relationship_Separated                    20838
relationship_Widowed                      20838
industry_Auto                             20838
industry_ClassAction                      20838
industry_Entertainment                    20838
industry_Other                            20838
industry_Pharma                           20838
industry_Political                        20838
genre_Comedy                              20838
genre_Direct                              20838
genre_Drama                               20838
genre_Infomercial                         20838
genre_Other                               20838
gender_Female                             20838
gender_Male                               20838
airtime_Daytime                           20838
airtime_Morning                           20838
airtime_Primetime                         20838
airlocation_Cambodia                      20838
airlocation_Canada                        20838
airlocation_China                         20838
airlocation_Columbia                      20838
                                          ...  
airlocation_Hungary                       20838
airlocation_India                         20838
airlocation_International                 20838
airlocation_Iran                          20838
airlocation_Ireland                       20838
airlocation_Italy                         20838
airlocation_Jamaica                       20838
airlocation_Japan                         20838
airlocation_Laos                          20838
airlocation_Mexico                        20838
airlocation_Nicaragua                     20838
airlocation_Outlying-US(Guam-USVI-etc)    20838
airlocation_Peru                          20838
airlocation_Philippines                   20838
airlocation_Poland                        20838
airlocation_Portugal                      20838
airlocation_Puerto-Rico                   20838
airlocation_Scotland                      20838
airlocation_South                         20838
airlocation_Taiwan                        20838
airlocation_Thailand                      20838
airlocation_Trinadad&Tobago               20838
airlocation_United-States                 20838
airlocation_Vietnam                       20838
airlocation_Yugoslavia                    20838
expensive_High                            20838
expensive_Low                             20838
expensive_Medium                          20838
money_back_guarantee_No                   20838
money_back_guarantee_Yes                  20838
Length: 73, dtype: int64
>>> traine.describe
<bound method NDFrame.describe of        runtime            ...             money_back_guarantee_Yes
id                        ...                                     
23855       40            ...                                    1
3068        40            ...                                    1
4230        30            ...                                    0
3515        40            ...                                    0
10404       40            ...                                    0
10770       20            ...                                    1
19973       38            ...                                    0
10229       50            ...                                    0
20605       60            ...                                    0
16183       40            ...                                    1
18911       43            ...                                    0
13997       54            ...                                    1
29659       35            ...                                    0
7010        55            ...                                    1
2550        40            ...                                    1
31481       36            ...                                    1
17273       40            ...                                    1
21288       55            ...                                    1
25782       40            ...                                    1
2736        20            ...                                    0
7491        40            ...                                    0
14923       40            ...                                    1
16309       36            ...                                    1
24599       46            ...                                    0
24424       50            ...                                    0
24164       35            ...                                    1
7802        50            ...                                    0
18650       37            ...                                    0
23352       45            ...                                    0
12989       40            ...                                    0
...        ...            ...                                  ...
7314        50            ...                                    1
3592        20            ...                                    0
30202       60            ...                                    0
2502        30            ...                                    0
30076       40            ...                                    0
4566        40            ...                                    1
19985       40            ...                                    1
20905       40            ...                                    0
18402       40            ...                                    1
3177        40            ...                                    1
28395       45            ...                                    0
27370       45            ...                                    1
10905       40            ...                                    1
18123       37            ...                                    0
25354       40            ...                                    0
30881       40            ...                                    1
22506       40            ...                                    1
25193       48            ...                                    1
31979       48            ...                                    0
984         24            ...                                    1
8902        40            ...                                    1
21079       65            ...                                    1
19914       40            ...                                    0
25387       50            ...                                    1
13020       25            ...                                    0
2770        40            ...                                    0
13722       40            ...                                    1
29935       40            ...                                    1
2934        40            ...                                    0
15969       37            ...                                    1

[20838 rows x 73 columns]>
>>> teste.describe
<bound method NDFrame.describe of        runtime            ...             money_back_guarantee_Yes
id                        ...                                     
5600        45            ...                                    1
22473       30            ...                                    1
7486        40            ...                                    1
164         40            ...                                    0
26794       48            ...                                    1
4100        40            ...                                    0
17304       50            ...                                    0
18965       20            ...                                    0
19686       40            ...                                    0
28586       55            ...                                    1
25053       55            ...                                    1
1576        10            ...                                    0
17037       40            ...                                    0
20365       18            ...                                    1
30233       50            ...                                    0
23662       40            ...                                    1
13833       60            ...                                    0
2734        50            ...                                    1
26313       25            ...                                    1
25190       46            ...                                    1
14700       45            ...                                    1
29089        8            ...                                    1
9960        48            ...                                    1
25360       40            ...                                    1
12782       40            ...                                    0
31771       40            ...                                    0
2336        35            ...                                    1
22573       98            ...                                    0
26644       46            ...                                    0
3456        40            ...                                    0
...        ...            ...                                  ...
27032       40            ...                                    1
19601       40            ...                                    1
3615        66            ...                                    1
6467        40            ...                                    0
21526       50            ...                                    1
13204       20            ...                                    0
16599       40            ...                                    1
30000       50            ...                                    1
2176        40            ...                                    1
17952       48            ...                                    0
14828       40            ...                                    0
14855       40            ...                                    1
18544       40            ...                                    0
12561       17            ...                                    0
21239       40            ...                                    0
18002       25            ...                                    1
31396       40            ...                                    0
30585       42            ...                                    0
29169       35            ...                                    1
538         40            ...                                    0
14917       45            ...                                    0
7634        40            ...                                    0
4836        30            ...                                    0
6575        30            ...                                    1
2149        40            ...                                    1
29104       40            ...                                    0
3810        50            ...                                    1
30735       20            ...                                    1
26529       30            ...                                    0
11043       40            ...                                    1

[5210 rows x 73 columns]>
>>> traine.to_csv('training_encoded.csv')
>>> teste.to_csv('test_encoded.csv')
>>> 
