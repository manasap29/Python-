%reset -f
#%%
# =============================================================================
# Data Structures
# =============================================================================
# 3 datatypes availabe,Series,DataFrame & Panel
# Series : 1 dimension,homogenious,data-mutable,size-immutable
# DataFrame : 2 dimensional,defined in rows & columns,heterogenious,data,size- mutable.
# Panel - 3 dimensional,heterogenious,data,size- mutable.

#%%
# pandas.Series : 

# capable of holding data of any type (integer, string, float, python objects, etc.).
# The axis labels are collectively called index.
# It can be created using various inputs like − Array, Dict, Scalar value or constant.

# empty series : 

import pandas as pd
x = pd.Series()
print(x)

# output : Series([], dtype: float64)

# Creating a Series from ndarray :

# If no index is passed to an ndarray, then by default index will be in range(n).

# Ex :

import pandas as pd
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
s = pd.Series(x)
print(s)

# output : 
#   0    1
#   1    2
#   2    3
#   3    4
#   4    5
#   5    6
#   6    7
#   7    8
#   8    9
#   dtype: int32

# if i will pass an index to the series it will look like this

# Ex :

import pandas as pd
import numpy as np
x = np.array(['a','b','c','d','e'])
s = pd.Series(x,index = [100,101,102,103,104])
print(s)

# output : 

#   100    a
#   101    b
#   102    c
#   103    d
#   104    e
#   dtype: object

# Creating a Series from dict :

# Ex :

import pandas as pd
import numpy as np
x = {'a' : 0., 'b' : 1., 'c' : 2., 'd' : 3., 'e' : 4., 'f' : 5., 'g' : 6., 'h' : 7., 'i' : 8.,'i' : 9.}
s = pd.Series(x)
print(s)

# output : 
#   a    0.0
#   b    1.0
#   c    2.0
#   d    3.0
#   e    4.0
#   f    5.0
#   g    6.0
#   h    7.0
#   i    9.0
#   dtype: float64

# Ex : missing data is filled with NaN

x = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(x,index=['b','c','d','a'])
print(s)

# output :

#   b    1.0
#   c    2.0
#   d    NaN
#   a    0.0
#   dtype: float64

# Creating a Series from Scalar : an index must be provided to the scalar value.

x = pd.Series(5, index=[0, 1, 2, 3, 4])
print(x)

# output :

#   0    5
#   1    5
#   2    5
#   3    5
#   4    5
#   dtype: int64

# Accessing Data from Series with Position

import pandas as pd
x = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])  
print(x[3:])

# output :
#   d    4
#   e    5
#   dtype: int64

print(x[1:3])

# output :
#   b    2
#   c    3
#   dtype: int64

print(x[:3])

# output :
#   a    1
#   b    2
#   c    3
#   dtype: int64

print(x[-3])
# output : 3

# Retrieving Data Using Label (Index)


# output : 1

print(x[['a','c','d']])

# output :

#   a    1
#   c    3
#  print(x['a']) d    4
#   dtype: int64

# print(x['f'])
# output : error is there as label is missing

# =============================================================================
# DataFrame
# =============================================================================

# 2 dimensional data structure,data alligned in rows & column.
# columns are of different types,Size – Mutable,Labeled axes (rows and columns)
# Can Perform Arithmetic operations on rows and columns
# A pandas DataFrame can be created using various inputs like −Lists,dict,Series,Numpy ndarrays,Another DataFrame
#%%
# Empty DataFrame :

import pandas as pd
df = pd.DataFrame()
print(df)

# output :

#   Empty DataFrame
#   Columns: []
#   Index: []

#%%
# DataFrame from Lists

# Ex:

import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

# output :
#      0
#   0  1
#   1  2
#   2  3
#   3  4
#   4  5

# Ex :

import pandas as pd
data = [['Aryan',2],['Arab',5],['Arpita',6]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

# output :

#        Name  Age
#   0   Aryan   2
#   1    Arab   5
#   2  Arpita   6

# we will display it as float

df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)

# output :

#        Name  Age
#   0   Aryan  2.0
#   1    Arab  5.0
#   2  Arpita  6.0

#%%
# DataFrame from Dict of ndarrays / Lists

data = {'name' : ['Aryan','Arab','Arpita','Adarsh','Ayush'], 'age' : [2,5,6,7,6]}
df = pd.DataFrame(data)
print(df)

# output :
#        name  age
#   0   Aryan    2
#   1    Arab    5
#   2  Arpita    6
#   3  Adarsh    7
#   4   Ayush    6

#%%
# DataFrame from List of Dicts

data = [{'key1' : 1,'key2' : 2},{'key3' : 3,'key4' : 4,'key5' : 5}]
df = pd.DataFrame(data)
print(df)

# output :

#      key1  key2  key3  key4  key5
#   0   1.0   2.0   NaN   NaN   NaN
#   1   NaN   NaN   3.0   4.0   5.0

# now we will define a row index

data = [{'key1' : 1,'key2' : 2},{'key3' : 3,'key4' : 4,'key5' : 5}]
df = pd.DataFrame(data, index = ['first','second'])
print(df)

# output :

#        key1  key2  key3  key4  key5
#first    1.0   2.0   NaN   NaN   NaN
#second   NaN   NaN   3.0   4.0   5.0


#%%
# DataFrame with a list of dictionaries, row indices, and column indices.

df1 = pd.DataFrame(data, index = ['first','second'], columns = ['key1', 'key2'])
print(df1)

# output :
#        key1  key2
#first    1.0   2.0
#second   NaN   NaN

df2 = pd.DataFrame(data, index = ['first','second'], columns = ['key1', 'key2', 'key3'])
print(df2)
#        key1  key2  key3
#first    1.0   2.0   NaN
#second   NaN   NaN   3.0

#%%
# DataFrame from Dict of Series

data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(data)
print(df)

# output:

#   one  two
#a  1.0    1
#b  2.0    2
#c  3.0    3
#d  NaN    4

# Column Selection

print(df['one'])

print()

# Column Addition

df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

df['four'] = pd.Series([40, 50, 60, 70], index=['a', 'b', 'c', 'd'])

print(df)
df = (df['one'] + df['three']),(df['two'] + df['four'])
print(df)

# output: 
#(a    11.0
#b    22.0
#c    33.0
#d     NaN
#dtype: float64, a    41
#b    52
#c    63
#d    74
#dtype: int64)

#%%
# Column Deletion

data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(data)
print(df)


del df['three']
print(df)


#%%
# Row Selection, Addition, and Deletion :Selection is done by "loc" function.

# label loc

data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(data)
print(df.loc['b'])

# output:
#one    2.0
#two    2.0
#Name: b, dtype: float64

#  by integer location

print(df.iloc[2])

# Slice Rows

print(df[2:4])

# Addition of Rows

df = pd.DataFrame([[1,2],[3,4]], columns = ['a','b'])

df1 = pd.DataFrame([[5,6],[7,8]], columns = ['a','b'])

df = df.append(df1)
print(df2)

# output:
#        key1  key2  key3
#first    1.0   2.0   NaN
#second   NaN   NaN   3.0


# Deletion of Rows
# We will use "drop" to delete.If label is duplicated, then multiple rows will be dropped.

df = df.drop(0)
df

# output:
#   a  b
#1  3  4
#1  7  8

#%%

# Panel : pandas.Panel() ,it can be created from ndarrays,dict of DataFrames

# It contains items − axis 0,major_axis − axis 1, it is the index (rows) of each of the DataFrames.
# minor_axis − axis 2, it is the columns of each of the DataFrames.

import numpy as np
import pandas as pd
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)

# output :

#<class 'pandas.core.panel.Panel'>
#Dimensions: 2 (items) x 4 (major_axis) x 5 (minor_axis)
#Items axis: 0 to 1
#Major_axis axis: 0 to 3
#Minor_axis axis: 0 to 4
#

#%%

# Basic Functionality :

#   axes :	Returns a list of the row axis labels.
#	dtype:	Returns the dtype of the object.
#	empty:	Returns True if series is empty.
#	ndim:	Returns the number of dimensions of the underlying data, by definition 1.
#	size:	Returns the number of elements in the underlying data.
#	values:Returns the Series as ndarray.
#	head()	: Returns the first n rows.
#	tail() :	Returns the last n rows.

import pandas as pd
import numpy as np

#Create a series with 100 random numbers
data = pd.Series(np.random.randn(4))
print(data)

print(data.axes)

print(data.empty)

print(data.ndim)

print(data.size)

print(data.values)


# The first two rows of the data series.
print(data.head(2))


# The last two rows of the data series.
print(data.tail(2))

# DataFrame Basic Functionality :

#	T	:   Transposes rows and columns.
#	axes:	Returns a list with the row axis labels and column axis labels as the only members.
#	dtypes :Returns the dtypes in this object.
#	empty:	True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
#	ndim:	Number of axes / array dimensions.
#	shape:	Returns a tuple representing the dimensionality of the DataFrame.
#	size:	Number of elements in the NDFrame.
#	values:Numpy representation of NDFrame.
#	head():Returns the first n rows.
#	tail():Returns last n rows.



import pandas as pd
import numpy as np


data = {'Name':pd.Series(['Aryan','Anshuman','Arab','Arnab','Adarsh','Ayush','Aadav']),
   'Age':pd.Series([2,4,3,6,7,8,9]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

df = pd.DataFrame(data)
print(df)

# output:

#       Name  Age  Rating
#0     Aryan    2    4.23
#1  Anshuman    4    3.24
#2      Arab    3    3.98
#3     Arnab    6    2.56
#4    Adarsh    7    3.20
#5     Ayush    8    4.60
#6     Aadav    9    3.80

# Transpose(T)

print(df.T)

# Axes
print(df.axes)

# dtypes
print(df.dtypes)

# empty
print(df.empty)

print(df.ndim)

print(df.shape)

print(df.size)

print(df.values)

# The first two rows of the data series.
print(df.head(2))


# The last two rows of the data series.
print(df.tail(2))


#%%

# Descriptive Statistics : sum(), mean(),std(),axis(),describe()..etc

#%%

# it uses the following important functions

#	count() :	Number of non-null observations
#	sum()	: Sum of values
#	mean()	: Mean of Values
#	median()	: Median of Values
#	mode()	: Mode of values
#	std()	: Standard Deviation of the Values
#	min()	: Minimum Value
#	max()	: Maximum Value
#	abs()	: Absolute Value
#	prod()	: Product of Values
#	cumsum()	: Cumulative Sum
#	cumprod()	: Cumulative Product



data = {'Name':pd.Series(['Aryan','Anshuman','Arab','Arnab','Adarsh','Ayush','Aadav']),
   'Age':pd.Series([2,4,3,6,7,8,9]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

df = pd.DataFrame(data)
print(df)

# output:

#       Name  Age  Rating
#0     Aryan    2    4.23
#1  Anshuman    4    3.24
#2      Arab    3    3.98
#3     Arnab    6    2.56
#4    Adarsh    7    3.20
#5     Ayush    8    4.60
#6     Aadav    9    3.80

# now we will apply describe()

print(df.describe())


# output()
#            Age    Rating
#count  7.000000  7.000000
#mean   5.571429  3.658571
#std    2.636737  0.698628
#min    2.000000  2.560000
#25%    3.500000  3.220000
#50%    6.000000  3.800000
#75%    7.500000  4.105000
#max    9.000000  4.600000


#  'include' is the argument which is used to pass necessary information
#  regarding what columns need to be considered for summarizing.

print(df.describe(include=['object']))

print(df.describe(include='all'))

#         Name       Age    Rating
#count       7  7.000000  7.000000
#unique      7       NaN       NaN
#top     Arnab       NaN       NaN
#freq        1       NaN       NaN
#mean      NaN  5.571429  3.658571
#std       NaN  2.636737  0.698628
#min       NaN  2.000000  2.560000
#25%       NaN  3.500000  3.220000
#50%       NaN  6.000000  3.800000
#75%       NaN  7.500000  4.105000
#max       NaN  9.000000  4.600000
#
# =============================================================================
# Function Application
# =============================================================================

# Three important methods are Table wise Function Application: pipe(),
# Row or Column Wise Function Application: apply(),Element wise Function Application: applymap()

#%%
# Table-wise Function Application : pipe()

# now we will add  a value 2 to all the elements in the DataFrame.

import numpy as np
import pandas as pd

def adder(ele1,ele2):
    return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns = ['col1','col2','col3'])
df.pipe(adder,2)

# output :
#       col1      col2      col3
#0  3.312446  1.973684  1.258262
#1  1.361364  2.516685  2.653126
#2  3.013351  1.580999  2.463236
#3  0.684762  3.727695 -0.162637
#4  1.833886  1.259820  1.693788

#%%

# Row or Column Wise Function Application :

# the operation performs column wise, taking each column as an array-like.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean)
print(df.apply(np.mean))

# By passing axis parameter, operations can be performed row wise.

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean,axis = 1)
print(df.apply(np.mean))

# Passing a lambda function to fine the max min diff. and calculate mean.

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(lambda x : x.max() - x.min())
print(df.apply(np.mean))


#%%

# Element Wise Function Application : methods applymap() on DataFrame and analogously map()
# on Series accept any Python function taking a single value and returning a single value.

# map method
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df['col1'].map(lambda x : x*100)
print(df.apply(np.mean))


# applymap method

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x : x*100)
print(df.apply(np.mean))

# =============================================================================
# Reindexing
# =============================================================================

# Reorder the existing data to match a new set of labels.

# Insert missing value (NA) markers in label locations where no data for the label existed.


# we will create a dataframe

index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
df = pd.DataFrame({
        'http_status': [200,200,404,404,301],
        'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]},
        
        index = index)

print(df)

# output :
#
#           http_status  response_time
#Firefox            200           0.04
#Chrome             200           0.02
#Safari             404           0.07
#IE10               404           0.08
#Konqueror          301           1.00

# now we will re index

new_index= ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10', 'Chrome']

df.reindex(new_index)

# output :
#               http_status  response_time
#Safari               404.0           0.07
#Iceweasel              NaN            NaN
#Comodo Dragon          NaN            NaN
#IE10                 404.0           0.08
#Chrome               200.0           0.02

# now We will fill in the missing values by passing a value to the keyword "fill_value"

df.reindex(new_index, fill_value=0)


#we can reindex the columns
df.reindex(new_index,columns = ['http_status', 'user_agent'])

# e will create a dataframe with a monotonically increasing index (for example, a sequence of dates)

import pandas as pd
import numpy as np

date_index = pd.date_range('1/1/2010', periods=12, freq='D')
df2 = pd.DataFrame({"prices": [100, 101, np.nan, 100, 89, 88,99,80,78,98,89,86]},index=date_index)
df2
        
# output
#            prices
#2010-01-01   100.0
#2010-01-02   101.0
#2010-01-03     NaN
#2010-01-04   100.0
#2010-01-05    89.0
#2010-01-06    88.0
#2010-01-07    99.0
#2010-01-08    80.0
#2010-01-09    78.0
#2010-01-10    98.0
#2010-01-11    89.0
#2010-01-12    86.0

# 
# reindex() takes an optional parameter method which is a filling method with values as follows −

# pad/ffill − Fill values forward

# bfill/backfill − Fill values backward

# nearest − Fill from the nearest index values

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values

print(df2.reindex_like(df1,method='ffill'))

# output

#       col1      col2      col3
#0  1.518944 -0.118813 -0.481718
#1  0.440418  0.893951  0.653781
#2  0.440418  0.893951  0.653781
#3  0.440418  0.893951  0.653781
#4  0.440418  0.893951  0.653781
#5  0.440418  0.893951  0.653781


# we can also limit whle filling
print(df2.reindex_like(df1,method='ffill',limit=1))

# =============================================================================
# Iteratind Dataframe
# =============================================================================

# iteritems() − to iterate over the (key,value) pairs
# iterrows() − iterate over the rows as (index,series) pairs
# itertuples() − iterate over the rows as namedtuples

# we will create a dtaaframe

import pandas as pd
import numpy as np

data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
		        'age': [20, 19, 22, 21],
		        'favorite_color': ['blue', 'red', 'yellow', "green"],
		        'grade': [88, 92, 95, 70]}

df =pd.DataFrame(data,columns = ['name', 'age', 'favorite_color', 'grade'])
df

# output
#
#               name  age favorite_color  grade
#0    Willard Morris   20           blue     88
#1       Al Jennings   19            red     92
#2      Omar Mullins   22         yellow     95
#3  Spencer McDaniel   21          green     70


# Iterate over rows in Pandas dataframe

for index, row in df.iterrows():
    print(row['name'],row['age'])

# output :
#
#Willard Morris 20
#Al Jennings 19
#Omar Mullins 22
#Spencer McDaniel 21
    
# Using itertuples:

for row in df.itertuples(index = True,name = 'pandas'):
    print(getattr(row,'name'),getattr(row,'age'))

# output :
#    
#Willard Morris 20
#Al Jennings 19
#Omar Mullins 22
#Spencer McDaniel 21

# If we wish to modify the rows yowe're iterating over, then df.apply is preferred.
    
def valuation_formula(x):
    return x * 0.5

df['age_half'] = df.apply(lambda row: valuation_formula(row['age']), axis=1)

df.head()

# output :

#               name  age favorite_color  grade  age_half
#0    Willard Morris   20           blue     88      10.0
#1       Al Jennings   19            red     92       9.5
#2      Omar Mullins   22         yellow     95      11.0
#3  Spencer McDaniel   21          green     70      10.5

# =============================================================================
# Sorting
# =============================================================================
#Pandas data frame has two useful functions
#sort_values(): to sort pandas data frame by one or more columns
#sort_index(): to sort pandas data frame by row index

df = pd.DataFrame({
     'col1' : ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2' : [2, 1, 9, 8, 7, 4],   'col3': [0, 1, 9, 4, 2, 3],})

df

# output:
  col1  col2  col3
0    A     2     0
1    A     1     1
2    B     9     9
3  NaN     8     4
4    D     7     2
5    C     4     3


# Sort by col1

df.sort_values(by = ['col1'])

# Sort by multiple columns

df.sort_values(by=['col1', 'col2'])

#Sort Descending

df.sort_values(by='col1', ascending = False)

#Putting NAs first

df.sort_values(by='col1', ascending=False, na_position='first')

    
#Sorting Algorithm

df.sort_values(by='col1', kind = 'mergesort')

# =============================================================================
# Working with Text Data
# =============================================================================

# Let us now see how each operation performs.
#
#	lower()	Converts strings in the Series/Index to lower case.

#	upper()	Converts strings in the Series/Index to upper case.

#	len()	Computes String length().

#	strip()	Helps strip whitespace(including newline) from each string in the Series/index from both the sides.

#	split(' ')	Splits each string with the given pattern.

#	cat(sep=' ')	Concatenates the series/index elements with given separator.

#	get_dummies()	Returns the DataFrame with One-Hot Encoded values.

#	contains(pattern)	Returns a Boolean value True for each element if the substring contains in the element, else False.

#	replace(a,b)	Replaces the value a with the value b.

#	repeat(value)	Repeats each element with specified number of times.

#	count(pattern)	Returns count of appearance of pattern in each element.

#	startswith(pattern)	Returns true if the element in the Series/Index starts with the pattern.

#	endswith(pattern)	Returns true if the element in the Series/Index ends with the pattern.

#	find(pattern)	Returns the first position of the first occurrence of the pattern.

#	findall(pattern)	Returns a list of all occurrence of the pattern.

#	swapcase	Swaps the case lower/upper.

#	islower()	Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean

#	isupper()	Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.

#	isnumeric()	Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.


# examples :


s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])

print(s)

print(s.str.lower())


print(s.str.upper())


print( s.str.len())


print(s.str.strip())

# split(pattern)

print(s.str.split(' '))

# cat(sep=pattern)

print(s.str.cat(sep='_'))


# get_dummies()

print( s.str.get_dummies())

#contains
print s.str.contains(' ')

#replace(a,b)

print(s.str.replace('@','$'))

# repeat(value)

print(s.str.repeat(2))

#count(pattern) : no of m in each string
print(s.str.count('m'))

#startswith(pattern)

print(s.str. startswith ('T'))

#endswith(pattern)
print(s.str.endswith('t'))

#find(pattern)

print(s.str.find('e'))

#findall(pattern)

print(s.str.findall('e'))


#swapcase()

print(s.str.swapcase())

#islower()
print(s.str.islower())
#
#isupper()
print(s.str.isupper())

#isnumeric()
print(s.str.isnumeric())


# =============================================================================
# Indexing and Selecting Data
# =============================================================================

# Pandas supports three types of Multi-axes indexing

# .loc()	Label based,.iloc()	Integer based,.ix()	Both Label and Integer based

#%%

# .loc() has multiple access methods like A single scalar label,A list of labels,A slice object,A Boolean array


# Ex- select all rows for a specific column

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print(df.loc[:,'A'])


# Select all rows for multiple columns, say list[]
print(df.loc[:,['A','C']])

# Select few rows for multiple columns, say list[]
print(df.loc[['a','b','f','h'],['A','C']])

# Select range of rows for all columns
print(df.loc['a':'h'])

# for getting values with a boolean array

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
print(df.loc['a']>0)

#%%

# .iloc() : An Integer,A list of integers,A range of values

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print(df.iloc[:4])


# Integer slicing
print(df.iloc[:4])
print(df.iloc[1:5, 2:4])

# Slicing through list of values
print(df.iloc[[1, 3, 5], [1, 3]])
print(df.iloc[1:3, :])
print (df.iloc[:,1:3])

#%%

# .ix()

df = pd.DataFrame(np.random.randn(8,4)),columns = ['A', 'B', 'C', 'D'])
print(df.A)

# =============================================================================
# Statistical Functions
# =============================================================================

# Percent_change : This function compares every element with its prior element and computes the change percentage.

import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print(df.pct_change())

# Covariance : to compute covariance between series objects

import pandas as pd
import numpy as np
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print(s1.cov(s2))

# when applied on a dataframe computes "cov" between columns.

import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print(frame['a'].cov(frame['b']))
print(frame.cov())

#Correlation :correlation shows the linear relationship between any two array of values (series).
# methods to compute the correlation like pearson(default), spearman and kendall.

import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])

print(frame['a'].corr(frame['b']))

print(frame.corr())

# Data Ranking
# Data Ranking produces ranking for each element in the array of elements. 
# In case of ties, assigns the mean rank.

s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))

s['d'] = s['b'] 
# so there's a tie

print(s.rank())

# =============================================================================
#  Missing Data
# =============================================================================

# Using reindexing, we have created a DataFrame with missing values.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

df

# check for missing values : isnull() and notnull() functions

print (df['one'].isnull())

print (df['one'].notnull())

# summing data

print(df['one'].sum())

#%%
# Cleaning / Filling Missing Data :

# Replace NaN with a Scalar Value

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one',
'two', 'three'])
    
# we will reindex
df = df.reindex(['a', 'b', 'c'])
print(df)

# NaN replaced with '0'.
print(df.fillna(0))

# Fill NA Forward and Backward
# pad/fill - 	Fill methods Forward
# bfill/backfill - Fill methods Backward

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df.fillna(method='pad'))

print(df.fillna(method='backfill'))

# Drop Missing Values :

print(df.dropna())

# Replace Missing (or) Generic Values

import pandas as pd
import numpy as np

df = pd.DataFrame({'one':[10,20,30,40,50,2000],
'two':[1000,0,30,40,50,60]})
    
print(df.replace({1000:10,2000:60}))

# =============================================================================
# GroupBy
# =============================================================================

# groupby operation involves Splitting the Object,Applying a function,Combining the results

# Ex:

import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print(df)

# output:

#      Team  Rank  Year  Points
#0   Riders     1  2014     876
#1   Riders     2  2015     789
#2   Devils     2  2014     863
#3   Devils     3  2015     673
#4    Kings     3  2014     741
#5    kings     4  2015     812
#6    Kings     1  2016     756
#7    Kings     1  2017     788
#8   Riders     2  2016     694
#9   Royals     4  2014     701
#10  Royals     1  2015     804
#11  Riders     2  2017     690

# Splittting data into groups

print(df.groupby('Team'))

print(df.groupby('Team').groups)


# grouping by multiple columns


print(df.groupby(['Team','Year']).groups)


# Iterating through Groups

grouped = df.groupby('Year')

for name,group in grouped:
    print(name)
    print(group)

# Selecting a group : get_group()
    
print(grouped.get_group(2014))


# Aggregations : single aggregated value for each group.

grouped = df.groupby('Year')
print(grouped['Points'].agg(np.mean))

grouped = df.groupby('Team')
print(grouped.agg(np.size))

# multiple aggregations

grouped = df.groupby('Team')
print(grouped['Points'].agg([np.sum, np.mean, np.std]))


# Transformations

score = lambda x: (x - x.mean()) / x.std()*10
print(grouped.transform(score))


#Filtration

print(df.groupby('Team').filter( lambda x:len(x) >=3))


# =============================================================================
# Merging/Joining
# =============================================================================

import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print(left)
print(right)


# Merging Two DataFrames on a Key

print(pd.merge(left, right,on = 'id'))

# output:
#
#   id  Name_x subject_id_x Name_y subject_id_y
#0   1    Alex         sub1  Billy         sub2
#1   2     Amy         sub2  Brian         sub4
#2   3   Allen         sub4   Bran         sub3
#3   4   Alice         sub6  Bryce         sub6
#4   5  Ayoung         sub5  Betty         sub5

# Two DataFrames on Multiple Keys

print(pd.merge(left,right,on = ['id','subject_id']))


# Using 'how' Argument:

# Left Join

print(pd.merge(left,right, on = 'subject_id', how = 'left'))


# right join

print(pd.merge(left, right, on='subject_id', how='right'))

# Outer Join

print(pd.merge(left, right, on='subject_id', how='outer'))

# inner join
print(pd.merge(left, right, on='subject_id', how='inner' ))


# =============================================================================
# concatenation
# =============================================================================

# combining together Series, DataFrame, and Panel objects.

import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print(pd.concat([one,two]))

# assigning keys to data frame

print(pd.concat([one,two],keys=['x','y']))

# we will ignore index / combining the index.The keys will be overidden
print(pd.concat([one,two],keys=['x','y'],ignore_index=True))

# we need to join them over axis,then it becomes
print(pd.concat([one,two],axis=1))

# Concatenating Using append : concatenate along axis=0,
print(one.append(two))

#%%
# Getting Current Time : datetime.now()

import pandas as pd
print(pd.datetime.now())

# Timestamp

print(pd.Timestamp('2018-07-29'))

# as per epoch :

import pandas as pd
print( pd.Timestamp(1532826900,unit='s'))

# Range of Time
print(pd.date_range('11:00','12:30',freq='30min').time)

#Changing the Frequency of Time
print(pd.date_range('11:00','16:30',freq='H').time)

# converting to timestamp,NaT is not a time
print(pd.to_datetime(pd.Series(['Jul 29, 2017','2016-10-28', None])))
