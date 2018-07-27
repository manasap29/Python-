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


































































