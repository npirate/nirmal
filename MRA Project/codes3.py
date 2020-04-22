Python 3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: E:\Google Drive\Ayurtantra LLC\Python Projects\MRA Project\Extract Diagnosis Codes 2.py 
Exported
>>> alld
        ID  All_ICD      ICD Disease
0        3    E1151    E1151      DM
1        4    E1151    E1151      DM
2       25    E1151    E1151      DM
3       52    E1151    E1151      DM
4      520    E1151    E1151      DM
5      682    E1151    E1151      DM
6      730    E1151    E1151      DM
7      791    E1151    E1151      DM
8     1089    E1151    E1151      DM
9     1112    E1151    E1151      DM
10    1136    E1151    E1151      DM
11    1152    E1151    E1151      DM
12    1229    E1151    E1151      DM
13    1378    E1151    E1151      DM
14    1997    E1151    E1151      DM
15    2099    E1151    E1151      DM
16    2124    E1151    E1151      DM
17       1    E1151    E1151      DM
18      80    E1151    E1151      DM
19      81    E1151    E1151      DM
20      86    E1151    E1151      DM
21      94    E1151    E1151      DM
22      95    E1151    E1151      DM
23      98    E1151    E1151      DM
24      99    E1151    E1151      DM
25     101    E1151    E1151      DM
26     113    E1151    E1151      DM
27     149    E1151    E1151      DM
28     158    E1151    E1151      DM
29     164    E1151    E1151      DM
...    ...      ...      ...     ...
2474  2545   C50411   C50411      CA
2475  1955     C775     C775      CA
2476  1994    J9620    J9620     CRF
2477  2104    J9620    J9620     CRF
2478  2065    C9112    C9112      CA
2479  2159    C3431    C3431      CA
2480  2168     C642     C642      CA
2481  2195   C50412   C50412      CA
2482  2201     C089     C089      CA
2483  2205     D420     D420      CA
2484  2205    D0322    D0322      CA
2485  2224    C9510    C9510      CA
2486  2224     D708     D708      ID
2487  2234    E1149    E1149      DM
2488  2236     C180     C180      CA
2489  2261     C434     C434      CA
2490  2297     D320     D320      CA
2491  2313    C8580    C8580      CA
2492  2316    J9691    J9691     CRF
2493  2358  E113593  E113593      DM
2494  2386    C3411    C3411      CA
2495  2387     C186     C186      CA
2496  2404   C50111   C50111      CA
2497  2445     D034     D034      CA
2498  2469  E113599  E113599      DM
2499  2494   E11638   E11638      DM
2500  2513     E138     E138      DM
2501  2514    I4821    I4821      AR
2502  2536     C140     C140      CA
2503  2545    C9200    C9200      CA

[2504 rows x 4 columns]
>>> alld.merge(alld, on = 'ID')
        ID All_ICD_x    ICD_x Disease_x All_ICD_y    ICD_y Disease_y
0        3     E1151    E1151        DM     E1151    E1151        DM
1        3     E1151    E1151        DM     E1142    E1142        DM
2        3     E1142    E1142        DM     E1151    E1151        DM
3        3     E1142    E1142        DM     E1142    E1142        DM
4        4     E1151    E1151        DM     E1151    E1151        DM
5       25     E1151    E1151        DM     E1151    E1151        DM
6       25     E1151    E1151        DM     E1142    E1142        DM
7       25     E1142    E1142        DM     E1151    E1151        DM
8       25     E1142    E1142        DM     E1142    E1142        DM
9       52     E1151    E1151        DM     E1151    E1151        DM
10      52     E1151    E1151        DM      N183     N183       CKD
11      52     E1151    E1151        DM     E1169    E1169        DM
12      52      N183     N183       CKD     E1151    E1151        DM
13      52      N183     N183       CKD      N183     N183       CKD
14      52      N183     N183       CKD     E1169    E1169        DM
15      52     E1169    E1169        DM     E1151    E1151        DM
16      52     E1169    E1169        DM      N183     N183       CKD
17      52     E1169    E1169        DM     E1169    E1169        DM
18     520     E1151    E1151        DM     E1151    E1151        DM
19     520     E1151    E1151        DM      N183     N183       CKD
20     520     E1151    E1151        DM     E1169    E1169        DM
21     520     E1151    E1151        DM     C9190    C9190        CA
22     520      N183     N183       CKD     E1151    E1151        DM
23     520      N183     N183       CKD      N183     N183       CKD
24     520      N183     N183       CKD     E1169    E1169        DM
25     520      N183     N183       CKD     C9190    C9190        CA
26     520     E1169    E1169        DM     E1151    E1151        DM
27     520     E1169    E1169        DM      N183     N183       CKD
28     520     E1169    E1169        DM     E1169    E1169        DM
29     520     E1169    E1169        DM     C9190    C9190        CA
...    ...       ...      ...       ...       ...      ...       ...
6350   991      C719     C719        CA      C700     C700        CA
6351   991      C700     C700        CA      C719     C719        CA
6352   991      C700     C700        CA      C700     C700        CA
6353  2260     E0840    E0840        DM     E0840    E0840        DM
6354  1022      E109     E109        DM      E109     E109        DM
6355  1103     I5041    I5041       CHF     I5041    I5041       CHF
6356  1528     C3491    C3491        CA     C3491    C3491        CA
6357  1557      D333     D333        CA      D333     D333        CA
6358  2285      C159     C159        CA      C159     C159        CA
6359  2076    C50911   C50911        CA    C50911   C50911        CA
6360  2512    C50911   C50911        CA    C50911   C50911        CA
6361  2225    C50411   C50411        CA    C50411   C50411        CA
6362  2401    C50411   C50411        CA    C50411   C50411        CA
6363  2545    C50411   C50411        CA    C50411   C50411        CA
6364  2545    C50411   C50411        CA     C9200    C9200        CA
6365  2545     C9200    C9200        CA    C50411   C50411        CA
6366  2545     C9200    C9200        CA     C9200    C9200        CA
6367  2159     C3431    C3431        CA     C3431    C3431        CA
6368  2201      C089     C089        CA      C089     C089        CA
6369  2234     E1149    E1149        DM     E1149    E1149        DM
6370  2236      C180     C180        CA      C180     C180        CA
6371  2261      C434     C434        CA      C434     C434        CA
6372  2313     C8580    C8580        CA     C8580    C8580        CA
6373  2316     J9691    J9691       CRF     J9691    J9691       CRF
6374  2404    C50111   C50111        CA    C50111   C50111        CA
6375  2445      D034     D034        CA      D034     D034        CA
6376  2469   E113599  E113599        DM   E113599  E113599        DM
6377  2494    E11638   E11638        DM    E11638   E11638        DM
6378  2514     I4821    I4821        AR     I4821    I4821        AR
6379  2536      C140     C140        CA      C140     C140        CA

[6380 rows x 7 columns]
>>> alld['ID','Disease']
Traceback (most recent call last):
  File "E:\Anaconda\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('ID', 'Disease')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    alld['ID','Disease']
  File "E:\Anaconda\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "E:\Anaconda\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "E:\Anaconda\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "E:\Anaconda\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "E:\Anaconda\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('ID', 'Disease')
>>> alld['ID'],['Disease']
(0          3
1          4
2         25
3         52
4        520
5        682
6        730
7        791
8       1089
9       1112
10      1136
11      1152
12      1229
13      1378
14      1997
15      2099
16      2124
17         1
18        80
19        81
20        86
21        94
22        95
23        98
24        99
25       101
26       113
27       149
28       158
29       164
        ... 
2474    2545
2475    1955
2476    1994
2477    2104
2478    2065
2479    2159
2480    2168
2481    2195
2482    2201
2483    2205
2484    2205
2485    2224
2486    2224
2487    2234
2488    2236
2489    2261
2490    2297
2491    2313
2492    2316
2493    2358
2494    2386
2495    2387
2496    2404
2497    2445
2498    2469
2499    2494
2500    2513
2501    2514
2502    2536
2503    2545
Name: ID, Length: 2504, dtype: int64, ['Disease'])
>>> alld[['ID'],['Disease']]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    alld[['ID'],['Disease']]
  File "E:\Anaconda\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "E:\Anaconda\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "E:\Anaconda\lib\site-packages\pandas\core\generic.py", line 2487, in _get_item_cache
    res = cache.get(item)
TypeError: unhashable type: 'list'
>>> alld[['ID']['Disease']]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    alld[['ID']['Disease']]
TypeError: list indices must be integers or slices, not str
>>> alld[['ICD','Disease']]
          ICD Disease
0       E1151      DM
1       E1151      DM
2       E1151      DM
3       E1151      DM
4       E1151      DM
5       E1151      DM
6       E1151      DM
7       E1151      DM
8       E1151      DM
9       E1151      DM
10      E1151      DM
11      E1151      DM
12      E1151      DM
13      E1151      DM
14      E1151      DM
15      E1151      DM
16      E1151      DM
17      E1151      DM
18      E1151      DM
19      E1151      DM
20      E1151      DM
21      E1151      DM
22      E1151      DM
23      E1151      DM
24      E1151      DM
25      E1151      DM
26      E1151      DM
27      E1151      DM
28      E1151      DM
29      E1151      DM
...       ...     ...
2474   C50411      CA
2475     C775      CA
2476    J9620     CRF
2477    J9620     CRF
2478    C9112      CA
2479    C3431      CA
2480     C642      CA
2481   C50412      CA
2482     C089      CA
2483     D420      CA
2484    D0322      CA
2485    C9510      CA
2486     D708      ID
2487    E1149      DM
2488     C180      CA
2489     C434      CA
2490     D320      CA
2491    C8580      CA
2492    J9691     CRF
2493  E113593      DM
2494    C3411      CA
2495     C186      CA
2496   C50111      CA
2497     D034      CA
2498  E113599      DM
2499   E11638      DM
2500     E138      DM
2501    I4821      AR
2502     C140      CA
2503    C9200      CA

[2504 rows x 2 columns]
>>> alld[['ICD','Disease']].merge(alld[['ICD','Disease']], on='ID')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    alld[['ICD','Disease']].merge(alld[['ICD','Disease']], on='ID')
  File "E:\Anaconda\lib\site-packages\pandas\core\frame.py", line 6389, in merge
    copy=copy, indicator=indicator, validate=validate)
  File "E:\Anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 61, in merge
    validate=validate)
  File "E:\Anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 551, in __init__
    self.join_names) = self._get_merge_keys()
  File "E:\Anaconda\lib\site-packages\pandas\core\reshape\merge.py", line 857, in _get_merge_keys
    rk, stacklevel=stacklevel))
  File "E:\Anaconda\lib\site-packages\pandas\core\generic.py", line 1382, in _get_label_or_level_values
    raise KeyError(key)
KeyError: 'ID'
>>> alld[['ID','Disease']].merge(alld[['ID','Disease']], on='ID')
        ID Disease_x Disease_y
0        3        DM        DM
1        3        DM        DM
2        3        DM        DM
3        3        DM        DM
4        4        DM        DM
5       25        DM        DM
6       25        DM        DM
7       25        DM        DM
8       25        DM        DM
9       52        DM        DM
10      52        DM       CKD
11      52        DM        DM
12      52       CKD        DM
13      52       CKD       CKD
14      52       CKD        DM
15      52        DM        DM
16      52        DM       CKD
17      52        DM        DM
18     520        DM        DM
19     520        DM       CKD
20     520        DM        DM
21     520        DM        CA
22     520       CKD        DM
23     520       CKD       CKD
24     520       CKD        DM
25     520       CKD        CA
26     520        DM        DM
27     520        DM       CKD
28     520        DM        DM
29     520        DM        CA
...    ...       ...       ...
6350   991        CA        CA
6351   991        CA        CA
6352   991        CA        CA
6353  2260        DM        DM
6354  1022        DM        DM
6355  1103       CHF       CHF
6356  1528        CA        CA
6357  1557        CA        CA
6358  2285        CA        CA
6359  2076        CA        CA
6360  2512        CA        CA
6361  2225        CA        CA
6362  2401        CA        CA
6363  2545        CA        CA
6364  2545        CA        CA
6365  2545        CA        CA
6366  2545        CA        CA
6367  2159        CA        CA
6368  2201        CA        CA
6369  2234        DM        DM
6370  2236        CA        CA
6371  2261        CA        CA
6372  2313        CA        CA
6373  2316       CRF       CRF
6374  2404        CA        CA
6375  2445        CA        CA
6376  2469        DM        DM
6377  2494        DM        DM
6378  2514        AR        AR
6379  2536        CA        CA

[6380 rows x 3 columns]
>>> alldf = alld[['ID','Disease']]
>>> alldf
        ID Disease
0        3      DM
1        4      DM
2       25      DM
3       52      DM
4      520      DM
5      682      DM
6      730      DM
7      791      DM
8     1089      DM
9     1112      DM
10    1136      DM
11    1152      DM
12    1229      DM
13    1378      DM
14    1997      DM
15    2099      DM
16    2124      DM
17       1      DM
18      80      DM
19      81      DM
20      86      DM
21      94      DM
22      95      DM
23      98      DM
24      99      DM
25     101      DM
26     113      DM
27     149      DM
28     158      DM
29     164      DM
...    ...     ...
2474  2545      CA
2475  1955      CA
2476  1994     CRF
2477  2104     CRF
2478  2065      CA
2479  2159      CA
2480  2168      CA
2481  2195      CA
2482  2201      CA
2483  2205      CA
2484  2205      CA
2485  2224      CA
2486  2224      ID
2487  2234      DM
2488  2236      CA
2489  2261      CA
2490  2297      CA
2491  2313      CA
2492  2316     CRF
2493  2358      DM
2494  2386      CA
2495  2387      CA
2496  2404      CA
2497  2445      CA
2498  2469      DM
2499  2494      DM
2500  2513      DM
2501  2514      AR
2502  2536      CA
2503  2545      CA

[2504 rows x 2 columns]
>>> alldf.merge(alldf, on='ID')
        ID Disease_x Disease_y
0        3        DM        DM
1        3        DM        DM
2        3        DM        DM
3        3        DM        DM
4        4        DM        DM
5       25        DM        DM
6       25        DM        DM
7       25        DM        DM
8       25        DM        DM
9       52        DM        DM
10      52        DM       CKD
11      52        DM        DM
12      52       CKD        DM
13      52       CKD       CKD
14      52       CKD        DM
15      52        DM        DM
16      52        DM       CKD
17      52        DM        DM
18     520        DM        DM
19     520        DM       CKD
20     520        DM        DM
21     520        DM        CA
22     520       CKD        DM
23     520       CKD       CKD
24     520       CKD        DM
25     520       CKD        CA
26     520        DM        DM
27     520        DM       CKD
28     520        DM        DM
29     520        DM        CA
...    ...       ...       ...
6350   991        CA        CA
6351   991        CA        CA
6352   991        CA        CA
6353  2260        DM        DM
6354  1022        DM        DM
6355  1103       CHF       CHF
6356  1528        CA        CA
6357  1557        CA        CA
6358  2285        CA        CA
6359  2076        CA        CA
6360  2512        CA        CA
6361  2225        CA        CA
6362  2401        CA        CA
6363  2545        CA        CA
6364  2545        CA        CA
6365  2545        CA        CA
6366  2545        CA        CA
6367  2159        CA        CA
6368  2201        CA        CA
6369  2234        DM        DM
6370  2236        CA        CA
6371  2261        CA        CA
6372  2313        CA        CA
6373  2316       CRF       CRF
6374  2404        CA        CA
6375  2445        CA        CA
6376  2469        DM        DM
6377  2494        DM        DM
6378  2514        AR        AR
6379  2536        CA        CA

[6380 rows x 3 columns]
>>> alldf.merge(alldf, on='ID', how='inner')
        ID Disease_x Disease_y
0        3        DM        DM
1        3        DM        DM
2        3        DM        DM
3        3        DM        DM
4        4        DM        DM
5       25        DM        DM
6       25        DM        DM
7       25        DM        DM
8       25        DM        DM
9       52        DM        DM
10      52        DM       CKD
11      52        DM        DM
12      52       CKD        DM
13      52       CKD       CKD
14      52       CKD        DM
15      52        DM        DM
16      52        DM       CKD
17      52        DM        DM
18     520        DM        DM
19     520        DM       CKD
20     520        DM        DM
21     520        DM        CA
22     520       CKD        DM
23     520       CKD       CKD
24     520       CKD        DM
25     520       CKD        CA
26     520        DM        DM
27     520        DM       CKD
28     520        DM        DM
29     520        DM        CA
...    ...       ...       ...
6350   991        CA        CA
6351   991        CA        CA
6352   991        CA        CA
6353  2260        DM        DM
6354  1022        DM        DM
6355  1103       CHF       CHF
6356  1528        CA        CA
6357  1557        CA        CA
6358  2285        CA        CA
6359  2076        CA        CA
6360  2512        CA        CA
6361  2225        CA        CA
6362  2401        CA        CA
6363  2545        CA        CA
6364  2545        CA        CA
6365  2545        CA        CA
6366  2545        CA        CA
6367  2159        CA        CA
6368  2201        CA        CA
6369  2234        DM        DM
6370  2236        CA        CA
6371  2261        CA        CA
6372  2313        CA        CA
6373  2316       CRF       CRF
6374  2404        CA        CA
6375  2445        CA        CA
6376  2469        DM        DM
6377  2494        DM        DM
6378  2514        AR        AR
6379  2536        CA        CA

[6380 rows x 3 columns]
>>> alldf.merge(alldf, on='ID', how='outer')
        ID Disease_x Disease_y
0        3        DM        DM
1        3        DM        DM
2        3        DM        DM
3        3        DM        DM
4        4        DM        DM
5       25        DM        DM
6       25        DM        DM
7       25        DM        DM
8       25        DM        DM
9       52        DM        DM
10      52        DM       CKD
11      52        DM        DM
12      52       CKD        DM
13      52       CKD       CKD
14      52       CKD        DM
15      52        DM        DM
16      52        DM       CKD
17      52        DM        DM
18     520        DM        DM
19     520        DM       CKD
20     520        DM        DM
21     520        DM        CA
22     520       CKD        DM
23     520       CKD       CKD
24     520       CKD        DM
25     520       CKD        CA
26     520        DM        DM
27     520        DM       CKD
28     520        DM        DM
29     520        DM        CA
...    ...       ...       ...
6350   991        CA        CA
6351   991        CA        CA
6352   991        CA        CA
6353  2260        DM        DM
6354  1022        DM        DM
6355  1103       CHF       CHF
6356  1528        CA        CA
6357  1557        CA        CA
6358  2285        CA        CA
6359  2076        CA        CA
6360  2512        CA        CA
6361  2225        CA        CA
6362  2401        CA        CA
6363  2545        CA        CA
6364  2545        CA        CA
6365  2545        CA        CA
6366  2545        CA        CA
6367  2159        CA        CA
6368  2201        CA        CA
6369  2234        DM        DM
6370  2236        CA        CA
6371  2261        CA        CA
6372  2313        CA        CA
6373  2316       CRF       CRF
6374  2404        CA        CA
6375  2445        CA        CA
6376  2469        DM        DM
6377  2494        DM        DM
6378  2514        AR        AR
6379  2536        CA        CA

[6380 rows x 3 columns]
>>> alldf
        ID Disease
0        3      DM
1        4      DM
2       25      DM
3       52      DM
4      520      DM
5      682      DM
6      730      DM
7      791      DM
8     1089      DM
9     1112      DM
10    1136      DM
11    1152      DM
12    1229      DM
13    1378      DM
14    1997      DM
15    2099      DM
16    2124      DM
17       1      DM
18      80      DM
19      81      DM
20      86      DM
21      94      DM
22      95      DM
23      98      DM
24      99      DM
25     101      DM
26     113      DM
27     149      DM
28     158      DM
29     164      DM
...    ...     ...
2474  2545      CA
2475  1955      CA
2476  1994     CRF
2477  2104     CRF
2478  2065      CA
2479  2159      CA
2480  2168      CA
2481  2195      CA
2482  2201      CA
2483  2205      CA
2484  2205      CA
2485  2224      CA
2486  2224      ID
2487  2234      DM
2488  2236      CA
2489  2261      CA
2490  2297      CA
2491  2313      CA
2492  2316     CRF
2493  2358      DM
2494  2386      CA
2495  2387      CA
2496  2404      CA
2497  2445      CA
2498  2469      DM
2499  2494      DM
2500  2513      DM
2501  2514      AR
2502  2536      CA
2503  2545      CA

[2504 rows x 2 columns]
>>> alldf.sort['ID']
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    alldf.sort['ID']
  File "E:\Anaconda\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'sort'
>>> alldf.sort(['ID'],ascending=[1])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    alldf.sort(['ID'],ascending=[1])
  File "E:\Anaconda\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'sort'
>>> alldf.sort_values(['ID'])
        ID Disease
17       1      DM
1452     1      DM
1453     3      DM
0        3      DM
1        4      DM
2156     5      DM
1454     7      DM
1455     8      DM
788     11      DM
651     16      DM
652     19      DM
2187    19      CA
106     20     CKD
789     21      DM
1135    21      AR
2193    21      DM
147     22     CKD
1643    22      DM
1456    22      DM
2188    23      CA
2       25      DM
1457    25      DM
1458    27      DM
790     27      DM
1459    28      DM
148     29     CKD
1460    31      DM
107     33     CKD
791     38      DM
792     41      DM
...    ...     ...
1221  2506      AR
2463  2512      CA
787   2513      DM
622   2513      AR
2500  2513      DM
1892  2513      DM
2501  2514      AR
1337  2515     CHF
1791  2516      DM
2186  2516      DM
1071  2517     CHF
1893  2517      DM
2249  2517     CRF
623   2517      AR
588   2518     CKD
2250  2524     CRF
2406  2524    COPD
589   2525     CKD
2389  2525      CA
750   2526      DM
751   2529      DM
2502  2536      CA
590   2539     CKD
2251  2544     CRF
2474  2545      CA
2503  2545      CA
1222  2546      AR
1838  2551      DM
2325  2558      CA
2348  2558      CA

[2504 rows x 2 columns]
>>> 
