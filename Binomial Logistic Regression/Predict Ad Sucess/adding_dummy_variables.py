Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> pd.read_csv('train.csv', index=col[0])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pd.read_csv('train.csv', index=col[0])
NameError: name 'col' is not defined
>>> pd.read_csv('train.csv', index_col=0)
         realtionship_status   ...   netgain
id                             ...          
19717  Married-spouse-absent   ...     False
31593     Married-civ-spouse   ...     False
5681                Divorced   ...     False
15491              Separated   ...     False
23587     Married-civ-spouse   ...      True
28523               Divorced   ...     False
12290     Married-civ-spouse   ...     False
20866          Never-married   ...     False
21312     Married-civ-spouse   ...     False
16479          Never-married   ...     False
9875           Never-married   ...     False
23314          Never-married   ...     False
9457      Married-civ-spouse   ...     False
6387           Never-married   ...     False
10499          Never-married   ...     False
27353  Married-spouse-absent   ...     False
52        Married-civ-spouse   ...     False
5380      Married-civ-spouse   ...      True
7209      Married-civ-spouse   ...     False
7660      Married-civ-spouse   ...      True
26880     Married-civ-spouse   ...     False
10217     Married-civ-spouse   ...      True
12594     Married-civ-spouse   ...     False
17290          Never-married   ...     False
29820                Widowed   ...     False
28656          Never-married   ...     False
23030     Married-civ-spouse   ...     False
5834                Divorced   ...      True
10943     Married-civ-spouse   ...     False
12404          Never-married   ...     False
...                      ...   ...       ...
13516     Married-civ-spouse   ...      True
13986          Never-married   ...     False
20293          Never-married   ...     False
30938     Married-civ-spouse   ...      True
21575          Never-married   ...     False
2005               Separated   ...     False
2227      Married-civ-spouse   ...     False
32186     Married-civ-spouse   ...     False
10817     Married-civ-spouse   ...     False
13093          Never-married   ...     False
10397          Never-married   ...     False
14055               Divorced   ...     False
19374          Never-married   ...     False
23099     Married-civ-spouse   ...     False
30927     Married-civ-spouse   ...     False
9543                Divorced   ...     False
679       Married-civ-spouse   ...     False
22422          Never-married   ...     False
26704               Divorced   ...     False
28446                Widowed   ...     False
17934          Never-married   ...     False
9921           Never-married   ...     False
28684               Divorced   ...     False
1933      Married-civ-spouse   ...     False
10827     Married-civ-spouse   ...     False
16009     Married-civ-spouse   ...      True
17241          Never-married   ...     False
2295      Married-civ-spouse   ...      True
17902          Never-married   ...     False
30877     Married-civ-spouse   ...     False

[26048 rows x 11 columns]
>>> df = pd.read_csv('train.csv', index_col=0)
>>> df.describe()
       average_runtime(minutes_per_week)       ratings
count                       26048.000000  26048.000000
mean                           40.294111      0.038716
std                            12.479457      0.075852
min                             1.000000      0.000000
25%                            40.000000      0.027465
50%                            40.000000      0.027465
75%                            45.000000      0.027465
max                            99.000000      1.000000
>>> df.columns
Index(['realtionship_status', 'industry', 'genre', 'targeted_sex',
       'average_runtime(minutes_per_week)', 'airtime', 'airlocation',
       'ratings', 'expensive', 'money_back_guarantee', 'netgain'],
      dtype='object')
>>> df = df.rename(columns ={'average_runtime(minutes_per_week)':'average_runtime_per_week','realtionship_status':'relationship_status'})
>>> df.columns
Index(['relationship_status', 'industry', 'genre', 'targeted_sex',
       'average_runtime_per_week', 'airtime', 'airlocation', 'ratings',
       'expensive', 'money_back_guarantee', 'netgain'],
      dtype='object')
>>> df = df.rename(columns ={'average_runtime_per_week':'runtime','realtionship_status':'relationship','targeted_sex':'gender'})
>>> df.columns
Index(['relationship_status', 'industry', 'genre', 'gender', 'runtime',
       'airtime', 'airlocation', 'ratings', 'expensive',
       'money_back_guarantee', 'netgain'],
      dtype='object')
>>> df = df.rename(columns = {'relationship_status':'relationship'})
>>> df.columns
Index(['relationship', 'industry', 'genre', 'gender', 'runtime', 'airtime',
       'airlocation', 'ratings', 'expensive', 'money_back_guarantee',
       'netgain'],
      dtype='object')
>>> df.describe
<bound method NDFrame.describe of                 relationship   ...   netgain
id                             ...          
19717  Married-spouse-absent   ...     False
31593     Married-civ-spouse   ...     False
5681                Divorced   ...     False
15491              Separated   ...     False
23587     Married-civ-spouse   ...      True
28523               Divorced   ...     False
12290     Married-civ-spouse   ...     False
20866          Never-married   ...     False
21312     Married-civ-spouse   ...     False
16479          Never-married   ...     False
9875           Never-married   ...     False
23314          Never-married   ...     False
9457      Married-civ-spouse   ...     False
6387           Never-married   ...     False
10499          Never-married   ...     False
27353  Married-spouse-absent   ...     False
52        Married-civ-spouse   ...     False
5380      Married-civ-spouse   ...      True
7209      Married-civ-spouse   ...     False
7660      Married-civ-spouse   ...      True
26880     Married-civ-spouse   ...     False
10217     Married-civ-spouse   ...      True
12594     Married-civ-spouse   ...     False
17290          Never-married   ...     False
29820                Widowed   ...     False
28656          Never-married   ...     False
23030     Married-civ-spouse   ...     False
5834                Divorced   ...      True
10943     Married-civ-spouse   ...     False
12404          Never-married   ...     False
...                      ...   ...       ...
13516     Married-civ-spouse   ...      True
13986          Never-married   ...     False
20293          Never-married   ...     False
30938     Married-civ-spouse   ...      True
21575          Never-married   ...     False
2005               Separated   ...     False
2227      Married-civ-spouse   ...     False
32186     Married-civ-spouse   ...     False
10817     Married-civ-spouse   ...     False
13093          Never-married   ...     False
10397          Never-married   ...     False
14055               Divorced   ...     False
19374          Never-married   ...     False
23099     Married-civ-spouse   ...     False
30927     Married-civ-spouse   ...     False
9543                Divorced   ...     False
679       Married-civ-spouse   ...     False
22422          Never-married   ...     False
26704               Divorced   ...     False
28446                Widowed   ...     False
17934          Never-married   ...     False
9921           Never-married   ...     False
28684               Divorced   ...     False
1933      Married-civ-spouse   ...     False
10827     Married-civ-spouse   ...     False
16009     Married-civ-spouse   ...      True
17241          Never-married   ...     False
2295      Married-civ-spouse   ...      True
17902          Never-married   ...     False
30877     Married-civ-spouse   ...     False

[26048 rows x 11 columns]>
>>> import numpy as np
>>> df['netgain'] = np.where(df['netgain'] & True, 1, 0)
>>> df.describe
<bound method NDFrame.describe of                 relationship   ...   netgain
id                             ...          
19717  Married-spouse-absent   ...         0
31593     Married-civ-spouse   ...         0
5681                Divorced   ...         0
15491              Separated   ...         0
23587     Married-civ-spouse   ...         1
28523               Divorced   ...         0
12290     Married-civ-spouse   ...         0
20866          Never-married   ...         0
21312     Married-civ-spouse   ...         0
16479          Never-married   ...         0
9875           Never-married   ...         0
23314          Never-married   ...         0
9457      Married-civ-spouse   ...         0
6387           Never-married   ...         0
10499          Never-married   ...         0
27353  Married-spouse-absent   ...         0
52        Married-civ-spouse   ...         0
5380      Married-civ-spouse   ...         1
7209      Married-civ-spouse   ...         0
7660      Married-civ-spouse   ...         1
26880     Married-civ-spouse   ...         0
10217     Married-civ-spouse   ...         1
12594     Married-civ-spouse   ...         0
17290          Never-married   ...         0
29820                Widowed   ...         0
28656          Never-married   ...         0
23030     Married-civ-spouse   ...         0
5834                Divorced   ...         1
10943     Married-civ-spouse   ...         0
12404          Never-married   ...         0
...                      ...   ...       ...
13516     Married-civ-spouse   ...         1
13986          Never-married   ...         0
20293          Never-married   ...         0
30938     Married-civ-spouse   ...         1
21575          Never-married   ...         0
2005               Separated   ...         0
2227      Married-civ-spouse   ...         0
32186     Married-civ-spouse   ...         0
10817     Married-civ-spouse   ...         0
13093          Never-married   ...         0
10397          Never-married   ...         0
14055               Divorced   ...         0
19374          Never-married   ...         0
23099     Married-civ-spouse   ...         0
30927     Married-civ-spouse   ...         0
9543                Divorced   ...         0
679       Married-civ-spouse   ...         0
22422          Never-married   ...         0
26704               Divorced   ...         0
28446                Widowed   ...         0
17934          Never-married   ...         0
9921           Never-married   ...         0
28684               Divorced   ...         0
1933      Married-civ-spouse   ...         0
10827     Married-civ-spouse   ...         0
16009     Married-civ-spouse   ...         1
17241          Never-married   ...         0
2295      Married-civ-spouse   ...         1
17902          Never-married   ...         0
30877     Married-civ-spouse   ...         0

[26048 rows x 11 columns]>
>>> df.columns
Index(['relationship', 'industry', 'genre', 'gender', 'runtime', 'airtime',
       'airlocation', 'ratings', 'expensive', 'money_back_guarantee',
       'netgain'],
      dtype='object')
>>> ohe = pd.get_dummies(df['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'])
Traceback (most recent call last):
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('relationship', 'industry', 'genre', 'gender', 'airtime', 'airlocation', 'expensive', 'money_back_guarantee')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ohe = pd.get_dummies(df['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'])
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('relationship', 'industry', 'genre', 'gender', 'airtime', 'airlocation', 'expensive', 'money_back_guarantee')
>>> ohe = pd.get_dummies(df,prefix = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'], columns = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'])
>>> ohe.columns
Index(['runtime', 'ratings', 'netgain', 'relationship_Divorced',
       'relationship_Married-AF-spouse', 'relationship_Married-civ-spouse',
       'relationship_Married-spouse-absent', 'relationship_Never-married',
       'relationship_Separated', 'relationship_Widowed', 'industry_Auto',
       'industry_ClassAction', 'industry_Entertainment', 'industry_Other',
       'industry_Pharma', 'industry_Political', 'genre_Comedy', 'genre_Direct',
       'genre_Drama', 'genre_Infomercial', 'genre_Other', 'gender_Female',
       'gender_Male', 'airtime_Daytime', 'airtime_Morning',
       'airtime_Primetime', 'airlocation_Cambodia', 'airlocation_Canada',
       'airlocation_China', 'airlocation_Columbia', 'airlocation_Cuba',
       'airlocation_Dominican-Republic', 'airlocation_Ecuador',
       'airlocation_El-Salvador', 'airlocation_England', 'airlocation_France',
       'airlocation_Germany', 'airlocation_Greece', 'airlocation_Guatemala',
       'airlocation_Haiti', 'airlocation_Holand-Netherlands',
       'airlocation_Honduras', 'airlocation_Hong', 'airlocation_Hungary',
       'airlocation_India', 'airlocation_International', 'airlocation_Iran',
       'airlocation_Ireland', 'airlocation_Italy', 'airlocation_Jamaica',
       'airlocation_Japan', 'airlocation_Laos', 'airlocation_Mexico',
       'airlocation_Nicaragua', 'airlocation_Outlying-US(Guam-USVI-etc)',
       'airlocation_Peru', 'airlocation_Philippines', 'airlocation_Poland',
       'airlocation_Portugal', 'airlocation_Puerto-Rico',
       'airlocation_Scotland', 'airlocation_South', 'airlocation_Taiwan',
       'airlocation_Thailand', 'airlocation_Trinadad&Tobago',
       'airlocation_United-States', 'airlocation_Vietnam',
       'airlocation_Yugoslavia', 'expensive_High', 'expensive_Low',
       'expensive_Medium', 'money_back_guarantee_No',
       'money_back_guarantee_Yes'],
      dtype='object')
>>> df = pd.get_dummies(df,prefix = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'], columns = ['relationship', 'industry', 'genre', 'gender', 'airtime','airlocation', 'expensive', 'money_back_guarantee'])
>>> df.columns
Index(['runtime', 'ratings', 'netgain', 'relationship_Divorced',
       'relationship_Married-AF-spouse', 'relationship_Married-civ-spouse',
       'relationship_Married-spouse-absent', 'relationship_Never-married',
       'relationship_Separated', 'relationship_Widowed', 'industry_Auto',
       'industry_ClassAction', 'industry_Entertainment', 'industry_Other',
       'industry_Pharma', 'industry_Political', 'genre_Comedy', 'genre_Direct',
       'genre_Drama', 'genre_Infomercial', 'genre_Other', 'gender_Female',
       'gender_Male', 'airtime_Daytime', 'airtime_Morning',
       'airtime_Primetime', 'airlocation_Cambodia', 'airlocation_Canada',
       'airlocation_China', 'airlocation_Columbia', 'airlocation_Cuba',
       'airlocation_Dominican-Republic', 'airlocation_Ecuador',
       'airlocation_El-Salvador', 'airlocation_England', 'airlocation_France',
       'airlocation_Germany', 'airlocation_Greece', 'airlocation_Guatemala',
       'airlocation_Haiti', 'airlocation_Holand-Netherlands',
       'airlocation_Honduras', 'airlocation_Hong', 'airlocation_Hungary',
       'airlocation_India', 'airlocation_International', 'airlocation_Iran',
       'airlocation_Ireland', 'airlocation_Italy', 'airlocation_Jamaica',
       'airlocation_Japan', 'airlocation_Laos', 'airlocation_Mexico',
       'airlocation_Nicaragua', 'airlocation_Outlying-US(Guam-USVI-etc)',
       'airlocation_Peru', 'airlocation_Philippines', 'airlocation_Poland',
       'airlocation_Portugal', 'airlocation_Puerto-Rico',
       'airlocation_Scotland', 'airlocation_South', 'airlocation_Taiwan',
       'airlocation_Thailand', 'airlocation_Trinadad&Tobago',
       'airlocation_United-States', 'airlocation_Vietnam',
       'airlocation_Yugoslavia', 'expensive_High', 'expensive_Low',
       'expensive_Medium', 'money_back_guarantee_No',
       'money_back_guarantee_Yes'],
      dtype='object')
>>> df.columns.str.strip()
Index(['runtime', 'ratings', 'netgain', 'relationship_Divorced',
       'relationship_Married-AF-spouse', 'relationship_Married-civ-spouse',
       'relationship_Married-spouse-absent', 'relationship_Never-married',
       'relationship_Separated', 'relationship_Widowed', 'industry_Auto',
       'industry_ClassAction', 'industry_Entertainment', 'industry_Other',
       'industry_Pharma', 'industry_Political', 'genre_Comedy', 'genre_Direct',
       'genre_Drama', 'genre_Infomercial', 'genre_Other', 'gender_Female',
       'gender_Male', 'airtime_Daytime', 'airtime_Morning',
       'airtime_Primetime', 'airlocation_Cambodia', 'airlocation_Canada',
       'airlocation_China', 'airlocation_Columbia', 'airlocation_Cuba',
       'airlocation_Dominican-Republic', 'airlocation_Ecuador',
       'airlocation_El-Salvador', 'airlocation_England', 'airlocation_France',
       'airlocation_Germany', 'airlocation_Greece', 'airlocation_Guatemala',
       'airlocation_Haiti', 'airlocation_Holand-Netherlands',
       'airlocation_Honduras', 'airlocation_Hong', 'airlocation_Hungary',
       'airlocation_India', 'airlocation_International', 'airlocation_Iran',
       'airlocation_Ireland', 'airlocation_Italy', 'airlocation_Jamaica',
       'airlocation_Japan', 'airlocation_Laos', 'airlocation_Mexico',
       'airlocation_Nicaragua', 'airlocation_Outlying-US(Guam-USVI-etc)',
       'airlocation_Peru', 'airlocation_Philippines', 'airlocation_Poland',
       'airlocation_Portugal', 'airlocation_Puerto-Rico',
       'airlocation_Scotland', 'airlocation_South', 'airlocation_Taiwan',
       'airlocation_Thailand', 'airlocation_Trinadad&Tobago',
       'airlocation_United-States', 'airlocation_Vietnam',
       'airlocation_Yugoslavia', 'expensive_High', 'expensive_Low',
       'expensive_Medium', 'money_back_guarantee_No',
       'money_back_guarantee_Yes'],
      dtype='object')
>>> 
