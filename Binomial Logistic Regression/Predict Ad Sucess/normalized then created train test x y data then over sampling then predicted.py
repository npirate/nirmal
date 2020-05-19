Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df = pd.read_csv('encoded.csv', index_col = [0])
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
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
NameError: name 'X' is not defined
>>> inport numpy as np
SyntaxError: invalid syntax
>>> import numpy as np
>>> X = np.array(df.ix[:,df.columns !='netgain'])

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: 
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

See the documentation here:
http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
>>> X = np.array(df.iloc(df.columns !='netgain'))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    X = np.array(df.iloc(df.columns !='netgain'))
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexing.py", line 98, in __call__
    axis = self.obj._get_axis_number(axis)
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\generic.py", line 365, in _get_axis_number
    axis = self._AXIS_ALIASES.get(axis, axis)
TypeError: unhashable type: 'numpy.ndarray'
>>> X = np.array (df.iloc[:, lambda df:[columns != 'netgain']])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    X = np.array (df.iloc[:, lambda df:[columns != 'netgain']])
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexing.py", line 1466, in __getitem__
    for x in key)
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexing.py", line 1466, in <genexpr>
    for x in key)
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\common.py", line 408, in _apply_if_callable
    return maybe_callable(obj, **kwargs)
  File "<pyshell#9>", line 1, in <lambda>
    X = np.array (df.iloc[:, lambda df:[columns != 'netgain']])
NameError: name 'columns' is not defined
>>> type (X)
<class 'numpy.ndarray'>
>>> x.shape
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x.shape
NameError: name 'x' is not defined
>>> X.shape
(26048, 72)
>>> X.describe
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    X.describe
AttributeError: 'numpy.ndarray' object has no attribute 'describe'
>>> X.describe()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    X.describe()
AttributeError: 'numpy.ndarray' object has no attribute 'describe'
>>> X.dtype
dtype('float64')
>>> X = np.arry (df.iloc[:, column != 'netgain'])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    X = np.arry (df.iloc[:, column != 'netgain'])
AttributeError: module 'numpy' has no attribute 'arry'
>>> X = np.array (df.iloc[:, column != 'netgain'])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    X = np.array (df.iloc[:, column != 'netgain'])
NameError: name 'column' is not defined
>>> X = np.array (df.iloc[:, columns != 'netgain'])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    X = np.array (df.iloc[:, columns != 'netgain'])
NameError: name 'columns' is not defined
>>> X = np.array(df.iloc[:,df.columns !='netgain'])
>>> y = np.array(df.iloc[:,df.columns =='netgain'])
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
>>> print ('Shape of X: {}'.format(X.shape))
Shape of X: (26048, 72)
>>> print('Shape of y: {}'.format(y.shape))
Shape of y: (26048, 1)
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=  0.3, random_state=0)
>>> print("Number transactions X_train dataset: ", X_train.shape)
print("Number transactions y_train dataset: ", y_train.shape)
print("Number transactions X_test dataset: ", X_test.shape)
print("Number transactions y_test dataset: ", y_test.shape)
SyntaxError: multiple statements found while compiling a single statement
>>> print("Number transactions X_train dataset: ", X_train.shape)
Number transactions X_train dataset:  (18233, 72)
>>> print("Number transactions y_train dataset: ", y_train.shape)

Number transactions y_train dataset:  (18233, 1)
>>> print("Number transactions X_test dataset: ", X_test.shape)

Number transactions X_test dataset:  (7815, 72)
>>> print("Number transactions y_test dataset: ", y_test.shape)

Number transactions y_test dataset:  (7815, 1)
>>> print("Before OverSampling, counts of label '1': {}".format(sum(y_train==1)))
Before OverSampling, counts of label '1': [4315]
>>> print("Before OverSampling, counts of label '0': {} \n".format(sum(y_train==0)))
Before OverSampling, counts of label '0': [13918] 

>>> 4315/13918
0.310030176749533
>>> from imblearn.over_sampling import SMOTE
>>> sm = SMOTE(random_state=2)
>>> X_train_res, y_train_res = sm.fit_sample(X_train, y_train.ravel())
>>> print('After OverSampling, the shape of train_X: {}'.format(X_train_res.shape))
After OverSampling, the shape of train_X: (27836, 72)
>>> print('After OverSampling, the shape of train_y: {} \n'.format(y_train_res.shape))
After OverSampling, the shape of train_y: (27836,) 

>>> y_train_res.shape
(27836,)
>>> print (y_train_res)
[0 0 1 ... 1 1 1]
>>> print("After OverSampling, counts of label '1': {}".format(sum(y_train_res==1)))
After OverSampling, counts of label '1': 13918
>>> print("After OverSampling, counts of label '0': {}".format(sum(y_train_res==0)))

After OverSampling, counts of label '0': 13918
>>> from sklearn.linear_model import LogisticRegression
>>> lr = LogisticRegression()
>>> lr.fit(X_train_res,y_train_res)

Warning (from warnings module):
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\linear_model\_logistic.py", line 939
    extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html.
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='auto', n_jobs=None, penalty='l2',
                   random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                   warm_start=False)
>>> lr = LogisticRegression(fit_intercept = False)
>>> lr.fit(X_train_res,y_train_res)

Warning (from warnings module):
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\linear_model\_logistic.py", line 939
    extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html.
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=False,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='auto', n_jobs=None, penalty='l2',
                   random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                   warm_start=False)
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
>>> from sklearn.preprocessing import StandardScaler
>>> df['normruntime','normratings'] = StandardScaler().fit_transform(np.array(df['runtime','ratings']).reshape(-1,1))
Traceback (most recent call last):
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('runtime', 'ratings')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    df['normruntime','normratings'] = StandardScaler().fit_transform(np.array(df['runtime','ratings']).reshape(-1,1))
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
KeyError: ('runtime', 'ratings')
>>> df['normruntime'] = StandardScaler().fit_transform(np.array(df['runtime']).reshape(-1,1))
>>> df['normratings'] = StandardScaler().fit_transform(np.array(df['ratings']).reshape(-1,1))
>>> df = df.drop(['runtime', 'ratings'], axis = 1)
>>> df.columns
Index(['netgain', 'relationship_Divorced', 'relationship_Married-AF-spouse',
       'relationship_Married-civ-spouse', 'relationship_Married-spouse-absent',
       'relationship_Never-married', 'relationship_Separated',
       'relationship_Widowed', 'industry_Auto', 'industry_ClassAction',
       'industry_Entertainment', 'industry_Other', 'industry_Pharma',
       'industry_Political', 'genre_Comedy', 'genre_Direct', 'genre_Drama',
       'genre_Infomercial', 'genre_Other', 'gender_Female', 'gender_Male',
       'airtime_Daytime', 'airtime_Morning', 'airtime_Primetime',
       'airlocation_Cambodia', 'airlocation_Canada', 'airlocation_China',
       'airlocation_Columbia', 'airlocation_Cuba',
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
       'money_back_guarantee_Yes', 'normruntime', 'normratings'],
      dtype='object')
>>> X = np.array(df.iloc[:,df.columns !='netgain'])
>>> y = np.array(df.iloc[:,df.columns =='netgain'])
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
>>> from imblearn.over_sampling import SMOTE
>>> sm = SMOTE(random_state=2)
>>> X_train_res, y_train_res = sm.fit_sample(X_train, y_train.ravel())
>>> from sklearn.linear_model import LogisticRegression
>>> lr = LogisticRegression(fit_intercept = False)
>>> lr.fit(X_train_res,y_train_res)

Warning (from warnings module):
  File "C:\Users\nimals\AppData\Local\Programs\Python\Python37-32\lib\site-packages\sklearn\linear_model\_logistic.py", line 939
    extra_warning_msg=_LOGISTIC_SOLVER_CONVERGENCE_MSG)
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html.
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=False,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='auto', n_jobs=None, penalty='l2',
                   random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                   warm_start=False)
>>> df['normratings']
id
19717   -0.148330
31593   -0.148330
5681    -0.148330
15491   -0.148330
23587   -0.148330
28523   -0.148330
12290   -0.148330
20866   -0.148330
21312   -0.148330
16479   -0.148330
9875    -0.148330
23314   -0.148330
9457     0.249534
6387    -0.148330
10499   -0.148330
27353   -0.148330
52      -0.148330
5380     1.778034
7209    -0.148330
7660    -0.148330
26880   -0.148330
10217    1.055135
12594   -0.148330
17290   -0.148330
29820   -0.148330
28656   -0.148330
23030   -0.148330
5834    -0.148330
10943   -0.148330
12404   -0.148330
           ...   
13516   -0.148330
13986   -0.148330
20293   -0.148330
30938   -0.148330
21575   -0.148330
2005    -0.148330
2227    -0.148330
32186    0.214402
10817    0.341211
13093   -0.148330
10397   -0.148330
14055   -0.148330
19374   -0.148330
23099   -0.148330
30927   -0.148330
9543    -0.148330
679     -0.148330
22422   -0.148330
26704   -0.148330
28446   -0.148330
17934   -0.148330
9921    -0.148330
28684   -0.148330
1933    -0.148330
10827   -0.148330
16009   -0.148330
17241   -0.148330
2295     0.837419
17902   -0.148330
30877   -0.148330
Name: normratings, Length: 26048, dtype: float64
>>> y_pred = lr.predict(X_test)
>>> print (classification_report(y_test,predications))
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print (classification_report(y_test,predications))
NameError: name 'classification_report' is not defined
>>> lr.score(X_test, y_test)
0.7621241202815099
>>> 
