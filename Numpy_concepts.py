#%%

%reset -f

#%%

# Basic data types

x = 5
print(type(x)) 
# Prints "<class 'int'>"

print(x)       
# Prints 3

print(x + 1)  
# Addition; prints 4

print(x - 1)   
# Subtraction; prints 2

print(x * 2)   
# Multiplication; prints 6

print(x ** 2)  
# Exponentiation; prints 9

x += 1
print(x)  
# Prints 4

x *= 2
print(x)  
# Prints 8

y = 2.5
print(type(y)) 
# Prints <class 'float'>

print(y, y + 1, y * 2, y ** 2) 
# Prints 2.5 3.5 5.0 6.25    

#%%
# Booleans

# It uses English words rather than symbols for Booleans logic

t = True
f = False

print(type(t)) 
# Prints <class 'bool'>

print(t and f) 
# Logical AND; prints False

print(t or f)  
# Logical OR; prints True

print(not t)   
# Logical NOT; prints False

print(t != f)  
# Logical XOR; prints True


#%%

# Strings: Python has great support for strings.

hello = 'hello'    
# String literals can use single quotes

world = "world"    
# or double quotes; it does not matter.

print(hello)       
# Prints hello

print(len(hello))  
# String length; prints 5

hw = hello + ' ' + world  
# String concatenation

print(hw)  
# prints hello world

hw12 = '%s %s %d' % (hello, world, 12)  
# sprintf style string formatting

print(hw12)  
# prints hello world 12


# Sring useful methods which are mostly used.

s = "hello"

print(s.capitalize())  
# Capitalize a string; prints Hello

print(s.upper())       
# Convert a string to uppercase; prints HELLO

print(s.rjust(7))      
# Right-justify a string, padding with spaces; prints   hello

print(s.center(7))     
# Center a string, padding with spaces; prints  hello 

print(s.replace('l', '(ell)'))  
# Replace all instances of one substring with another;
# prints he(ell)(ell)o
                                
print('  world '.strip())  
# Strip leading and trailing whitespace; prints world

#%%
# Containers

# Python includes several built-in container types: lists, dictionaries, sets, and tuples.
#%%
# Lists

xs = [3, 1, 2]    
# Create a list

print(xs, xs[2])  
# Prints [3, 1, 2] 2

print(xs[-1])     
# Negative indices count from the end of the list; prints 2

xs[2] = 'foo'     
# Lists can contain elements of different types

print(xs)         
# Prints [3, 1, 'foo']

xs.append('bar')  
# Add a new element to the end of the list

print(xs)         
# Prints [3, 1, 'foo', 'bar']

x = xs.pop()      
# Remove and return the last element of the list

print(x, xs)      
# Prints bar [3, 1, 'foo']


# Slicing:Python provides concise syntax to access sublists; this is known as slicing:

nums = list(range(5))     
# range is a built-in function that creates a list of integers

print(nums)               
# Prints [0, 1, 2, 3, 4]

print(nums[2:4])          
# Get a slice from index 2 to 4 (exclusive); prints [2, 3]

print(nums[2:])           
# Get a slice from index 2 to the end; prints [2, 3, 4]

print(nums[:2])           
# Get a slice from the start to index 2 (exclusive); prints [0, 1]

print(nums[:])            
# Get a slice of the whole list; prints [0, 1, 2, 3, 4]

print(nums[:-1])          
# Slice indices can be negative; prints [0, 1, 2, 3]

nums[2:4] = [8, 9]        
# Assign a new sublist to a slice

print(nums)               
# Prints [0, 1, 8, 9, 4]


# Loops: we can loop over the elements of a list

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# Prints 
# cat
# dog
# monkey 
    
# List comprehensions:
    
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)   
# Prints [0, 1, 4, 9, 16]

# we can make this code simpler using a list comprehension

nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   
# Prints [0, 1, 4, 9, 16]


# List comprehensions can also contain conditions

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  
# Prints [0, 4, 16]

#%%
# Dictionaries : A dictionary stores (key, value) pairs.

d = {'cat': 'cute', 'dog': 'furry'}  
# Create a new dictionary with some data

print(d['cat'])       
# Get an entry from a dictionary; prints cute

print('cat' in d)     
# Check if a dictionary has a given key; prints True

d['fish'] = 'wet'     
# Set an entry in a dictionary

print(d['fish'])      
# Prints wet

# print(d['monkey'])  
# KeyError: 'monkey' not a key of d

print(d.get('monkey', 'N/A'))  
# Get an element with a default; prints N/A

print(d.get('fish', 'N/A'))    
# Get an element with a default; prints wet

del d['fish']         
# Remove an element from a dictionary

print(d.get('fish', 'N/A'))
# "fish" is no longer a key; prints N/A


# Loops: It is easy to iterate over the keys in a dictionary

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))
# Prints 
# A person has 2 legs
# A cat has 4 legs
# A spider has 8 legs
    
# If we want access to keys and their corresponding values, use the items method
    
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))
# Prints 
# A person has 2 legs
# A cat has 4 legs
# A spider has 8 legs

# Dictionary comprehensions
    
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  
# Prints {0: 0, 2: 4, 4: 16}
#%%
# Sets :A set is an unordered collection of distinct elements.

animals = {'cat', 'dog'}
print('cat' in animals)   
# Check if an element is in a set; prints True

print('fish' in animals)  
# prints False

animals.add('fish')      
# Add an element to a set

print('fish' in animals)  
# Prints True

print(len(animals))       
# Number of elements in a set; prints 3

animals.add('cat')        
# Adding an element that is already in the set does nothing

print(len(animals))      
# Prints 3

animals.remove('cat')     
# Remove an element from a set

print(len(animals))       
# Prints 2

# Loops: Iterating over a set has the same syntax as iterating over a list.

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints 
#1: dog
#2: fish
#3: cat
    
# Set comprehensions
    
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)  
# Prints {0, 1, 2, 3, 4, 5}          
#%%
# Tuples : A tuple is an (immutable) ordered list of values

d = {(x, x + 1): x for x in range(10)}  
# Create a dictionary with tuple keys

t = (5, 6)        
# Create a tuple

print(type(t))    
# Prints "<class 'tuple'>"

print(d[t])       
# Prints 5

print(d[(1, 2)])  
# Prints 1
#%%
# Functions : Python functions are defined using the def keyword

def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))
    
# Prints 
# negative
# zero
# positive


def hello(name, loud=False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s' % name)

hello('Bob')
# Prints Hello, Bob

hello('Fred', loud=True) 
# Prints HELLO, FRED!
#%%
# Classes
# The syntax for defining classes in Python is straightforward

class Greeter(object):

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

g = Greeter('Fred')  
# Construct an instance of the Greeter class

g.greet()            
# Call an instance method; prints "Hello, Fred"

g.greet(loud=True)   
# Call an instance method; prints "HELLO, FRED!"

#%%

# Numpy

# A numpy array is a grid of values, all of the same type, and is indexed by a 
# tuple of nonnegative integers.

import numpy as np

a = np.array([1, 2, 3])   
# Create a rank 1 array

print(type(a))            
# Prints "<class 'numpy.ndarray'>"

print(a.shape)            
# Prints (3,)

print(a[0], a[1], a[2])   
# Prints 1 2 3

a[0] = 5                  
# Change an element of the array

print(a)                  
# Prints [5 2 3]


b = np.array([[1,2,3],[4,5,6]])    
# Create a rank 2 array

print(b.shape)                     
# Prints (2, 3)

print(b[0, 0], b[0, 1], b[1, 0])   
# Prints 1 2 4

#%%
# Numpy also provides many functions to create arrays

import numpy as np

a = np.zeros((2,2))   
# Create an array of all zeros
print(a)              
# Prints [[0. 0.]
# [0. 0.]]


b = np.ones((1,2))    
# Create an array of all ones
print(b)              
# Prints [[ 1.  1.]]

c = np.full((2,2), 7)  
# Create a constant array
print(c)               
# Prints 
#[[7 7]
# [7 7]]

d = np.eye(2)         
# Create a 2x2 identity matrix
print(d)              
# Prints 
# [[1. 0.]
# [0. 1.]]


e = np.random.random((2,2))  
# Create an array filled with random values
print(e)    
                 
# [[0.34546416 0.94700657]
# [0.81877976 0.32990396]]
#%%
# Array indexing

#%%
# Slicing: Similar to Python lists, numpy arrays can be sliced.

import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.

print(a[0, 1])   
# Prints 2

b[0, 0] = 77     
# b[0, 0] is the same piece of data as a[0, 1]

print(a[0, 1])   
# Prints 77
#%%
# we can also mix integer indexing with slice indexing.

import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])


# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:

row_r1 = a[1, :]    
# Rank 1 view of the second row of a

row_r2 = a[1:2, :]  
# Rank 2 view of the second row of a

print(row_r1, row_r1.shape)  
# Prints [5 6 7 8] (4,)

print(row_r2, row_r2.shape) 
# Prints [[5 6 7 8]] (1, 4)

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]

print(col_r1, col_r1.shape)  
# Prints [ 2  6 10] (3,)

print(col_r2, col_r2.shape)  
# Prints [[ 2]
# [ 6]
# [10]] (3, 1)


#%% 
# Integer array indexing: 

# When we index into numpy arrays using slicing, the resulting array view will
# always be a subarray of the original array

import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])

# An example of integer array indexing.

# The returned array will have shape (3,) 
print(a[[0, 1, 2], [0, 1, 0]])  
# Prints [1 4 5]

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  
# Prints [1 4 5]

# When using integer array indexing, we can reuse the same
# element from the source array:
print(a[[0, 0], [1, 1]])  
# Prints [2 2]

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]]))  
# Prints [2 2]

# The trick with integer array indexing is selecting or mutating one element from 
# each row of a matrix.

import numpy as np

# Create a new array from which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print(a)  
# prints [[ 1  2  3]
# [ 4  5  6]
# [ 7  8  9]
# [10 11 12]]
#    
# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  
# Prints [ 1  6  7 11]

# Mutate one element from each row of a using the indices in b
a[np.arange(4), b] += 10

print(a)  
# prints 
# [[11  2  3]
# [ 4  5 16]
# [17  8  9]
# [10 21 12]]
#%%
# Boolean array indexing:

# It let's us pick arbitrary ellements in the array

import numpy as np

a =  np.array([[1,2],[3,4],[5,6]])
bool_idx = (a > 2)
print(bool_idx)

# Prints
[[False False]
 [ True  True]
 [ True  True]]
# We use boolean array index to construct an array of rank 1.

print(a[bool_idx])

#%%
# numpy.array

# The most important object defined in numpy is a N dimensional array called ndarry.
# It describes the collection of items of same data type.
# Each element in ndarray is called an object of data type object(dtype)  
# An object extracted from ndarray object(slicing) is represented by a python object
# of one of array scalar types.  
# The basic ndarray is created using an array function in numpy.

# with one dimension
import numpy as np
a = np.array([1,2,3])
print(a)
    
# with two dimension

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)

# Minimum dimension

import numpy as np
a = np.array([1,2, 3,4,5], ndmin = 2)
print(a)

# dtype parameter
a = np.array([1,2,3], dtype = complex)
print(a)
#%%
# numpy data types 
#
# bool_ : T/F stored as bye
# int_ : default integer type
# intc : Identical to C integer    
# intp : integer sd for indexing
# int8 : byte
# int16 : integer(range)
# int32 : integer(range)
# int64 : integer(range)
# uint8 : Unsigned integer
# uint16 : Unsigned integer
# uint32 : Unsigned integer
# uint64 : Unsigned integer
# float_ : shorthand for float64
# float16 :
# float32 :
# float64 :
# complex_ :
# complex64 :
# complex128 :

# Data type objects(dtype) : It describes a fixed block of memory corresponding
# to an array depending on :  
# Type of data,size of data,byte order(little ending or big ending),in case of structured
# data type name of each field,datatype of each field and memory taken by each block.
# If data is subarray,it's shape and data type.

# A dtype object is constructed using the following syntax :

numpy.dtype(object, allign, copy)

# Object − To be converted to data type object

# Align − If true, adds padding to the field to make it similar to C-struct

# Copy − Makes a new copy of dtype object. If false, the result is reference to builtin data type object

import numpy as np
dt = np.dtype(np.int32)
print(dt)

# output : int32

# int8,int16,int32,int64 can be replaced by equivalent string i1,i2,i4 etc.
import numpy as np
dt = np.dtype('i4')
print(dt)

# output : int32

# using endian notation

import numpy as np
dt = np.dtype('>i4')
print(dt)
# output : >i4

# Let's create a structured data type

import numpy as np
dt = np.dtype([('age',np.int8)])
print(dt)

# output : [('age', 'i1')]

# Let's apply it to ndarray object
import numpy as np
dt = np.dtype([('age',np.int8)])
a = np.array([(10),(20),(30)], dtype = dt)
print(a)

# output:  [(10,) (20,) (30,)]

# file name can be used for accessing the content of the columns

import numpy as np
dt = np.dtype([('age',np.int8)])
a = np.array([(10),(20),(30)])
print(a)

# output : [10 20 30]

# Ex: wher the data type is assigned to ndarray object.
 
import numpy as np
student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)

import numpy as np 

    student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
    a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
    print(a)

# Each builtin dta type has a character code that uniquely identifies it.
    
# 'b' − boolean

# 'i' − (signed) integer

# 'u' − unsigned integer

# 'f' − floating-point

# 'c' − complex-floating point

# 'm' − timedelta

# 'M' − datetime

# 'O' − (Python) objects

# 'S', 'a' − (byte-)string

# 'U' − Unicode

#' V' − raw data (void)

#%%
# Array attributes:

# the array attributes returns a tuple consisting of array dimensions.It is also used for 
# resizing the array.
#%%    
# ndarray.shape
    
import numpy as np,
a = np.array([[1,2,3],[4,5,6]])    
print(a.shape)

# output: 
# (2, 3)
#%%

# It resizes the ndarray

import numpy as np
a =np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)

# output :  
# [[1 2]
# [3 4]
# [5 6]]

#%%

# it also provides a reshape function to resize an array.

import numpy as np
a =np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)

# output :
# [[1 2]
# [3 4]
# [5 6]]

#%%
# ndarray.ndim

# This array attribute returns the number of array dimensions.

# an array of evenly spaced numbers

import numpy as np
a = np.arange(24)
print(a)

# output: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

#%%

# This is onedimensional array

import numpy as np
a = np.arange(24)
a.ndim
    
# now let's reshape it.
b = a.reshape(2,4,3)
print(b)

# output:
#[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]]

# [[12 13 14]
  [15 16 17]
  [18 19 20]
  [21 22 23]]]

#%%

# numpy.itemsize

# This array attribute returns the length of each element of array in bytes.

# dtype of array in int8(1 byte)

import numpy as np
x = np.array([1,2,3,4,5],dtype = np.int8)
print(x.itemsize)

# output : 1



# dtype of array in float32(4 byte)

import numpy as np
x = np.array([1,2,3,4,5],dtype = np.float32)
print(x.itemsize)

# output : 4

#%%

# numpy.flags

# "ndarray" has the following attributes.

# Atributes & Description

#  C_CONTIGUOUS 
#  F_CONTIGUOUS 
#  OWNDATA 
#  WRITEABLE 
#  ALIGNED
#  WRITEBACKIFCOPY 
#  UPDATEIFCOPY 

import numpy as np
x = np.array([1,2,3,4,5])
print(x.flags)

# output:   
#  C_CONTIGUOUS : True
#  F_CONTIGUOUS : True
#  OWNDATA : True
#  WRITEABLE : True
#  ALIGNED : True
#  WRITEBACKIFCOPY : False
#  UPDATEIFCOPY : False

#%%

# ARRAY CREATION ROUTINES :

#%%

# numpy.empty

# it creates an uninitialized array of specific shape and dtype.The constructor is
# numpy.empty(shape.dtype = float, order = 'C')
        
# Shape
# Shape of an empty array in int or tuple of int

# Dtype
# Desired output data type. 

# Order
# 'C' for C-style row-major array, 'F' for FORTRAN style column-major array
#%%
# numpy.zeros

# Returns a specified array of specified size filled with zeros.

# Array of five zeros.default dtype is float.

import numpy as np
x = np.zeros(5)
print(x)

# output : [0. 0. 0. 0. 0.]

import numpy as np
x = np.zeros((5,), dtype = np.int)
print(x)
# output : [0. 0. 0. 0. 0.]

# custom type:

import numpy as np 
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  
print (x)

# output : 
#[[(0, 0) (0, 0)]
# [(0, 0) (0, 0)]]

#%%
# numpy.ones 

# numpy.ones : Returns a new array of specified size and type
# the constructor of the numpy.ones is.. 
# numpy.ones(shape, dtype = None, order = 'C').It takes # Shape # Dtype # Order.

import numpy as np
x =np.ones(5)
print(x)

# output: [1. 1. 1. 1. 1.]

import numpy as np
x = np.ones([2,2])
print(x)

# output : 
#[[1. 1.]
# [1. 1.]]

#%%

# Array of existing data: 
# Creation of an array from an existing data.

#%%
# numpy.asarray

# It is same as numpy.array but has fewer parameters.
# The constructor is ... numpy.asarray(a, dtype = None, order = None)
# The parameters it takes is a, dttype, order.

# converting a list to ndarray    
import numpy as np
x = [1,2,3]
a = np.asarray(x)
print(a)

# dtype is set
import numpy as np
x = [1,2,3]
a = np.asarray(x, dtype = float)
print(a)

# ndarray from a tuple
import numpy as np
x = (1,2,3)
a = np.asarray(x)
print(a)

# ndarray from list of tuples 
import numpy as np 
x = [(1,2,3),(4,5)] 
a = np.asarray(x) 
print a

#%%

# numpy.frombuffer

# This function interprets a buffer as one-dimensional array.
# The constructor is... numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
# The parameters it takes are buffer,dtype,count,offset.

# Ex-1

import numpy as np 
s = 'Hello World' 
a = np.frombuffer(s, dtype = 'S1') 
print (a)
#%%
    
# numpy.fromiter

# It builds an ndarray object from any iterable object.
# A new one dimensional array is returned 
# The constructor... numpy.fromiter(iterable, dtype, count = -1)
# It takes parameter iterable,dtype & count.


# let's use the built-in range() function to return a list object
import numpy as np 
list = range(5) 
print(list)

# obtain iterator object from list 
import numpy as np 
list = range(5) 
it = iter(list)  

# use iterator to create ndarray 
x = np.fromiter(it, dtype = float) 
print(x)

#%%

# numpy.arange

# It returns a evely spaced values within a given range.
# The cnstructor is... numpy.arange(start, stop, step, dtype)
# The parameter passed are start,stop,step & dtype.

# ex1

import numpy as np
x =np.arange(5)
print(x)

# ex2 -  dtype is a set

import numpy as np
x = np.arange(5, dtype = float)
print(x)

# ex3

# start and stop parameters set
import numpy as np
x = np.arange(10,20,2)
print(x)

#%%
# numpy.linespace

# This is like arange but the number of evenly spaced values between the interval is specified .
# The parametre passed into is start,stop,num,endpoint,retstep,dtype.

# Ex1 

import numpy as np 
x = np.linspace(10,20,5) 
print(x)

# endpoint set to false
import numpy as np
x = np.linspace(10,20,5,endpoint = False)
print(x)

# let's check retstep
import numpy as np
x = np.linspace(1,2,5, retstep = True)
print(x)

#%%
# numpy.logspace

# it returns an ndarray object the number that are evenly spaced on a logscale.
# Parameters passed are start,stop,num,endpoint,base,dtype.

import numpy as np 

# default base is 10 
a = np.logspace(1.0, 2.0, num = 10) 
print(a)

# let's set the base to 2.
# set base of log space to 2 
import numpy as np 
a = np.logspace(1,10,num = 10, base = 2) 
print(a)

#%%
# Indexing and slicing

# Three types of indexing methods are available − field access,
# basic slicing and advanced indexing.

# ex1

import numpy as np 
a = np.arange(10) 
s = slice(2,7,2) 
print(a[s])

# Ex2 : slice single item 

import numpy as np 
a = np.arange(10) 
b = a[5] 
print(b)

#Ex3 : slice items starting from index 
import numpy as np 
a = np.arange(10) 
print(a[2:])

# ex4 : slice items between indexes 
import numpy as np 
a = np.arange(10) 
print(a[2:5])

# ex5 : import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print(a)  

# slice items starting from index
print ('Let us slice the array from the index a[1:]')
print(a[1:])


# array to begin with
import numpy as  np
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print('The array is: ')
print(a)
print('\n')

# below will return the the array of 2nd column
print('the second item is:')
print(a[...,1])
print('\n')

# we can slice all items from the second row this way
print('The items in the second row are:')
print (a[1,...] )
print('\n')  

# Now we will slice all items from column 1 onwards 
print('The items column 1 onwards are:')
print( a[...,1:])

#%%
# Advanced indexing

# There are two types of advanced indexing Integer & Boolean.
#%%
# ex -1

import numpy as np 

x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,1,2], [0,1,0]] 
print(y)

# The selection includes elements at (0,0), (1,1) and (2,0) from the first array.
# here the indexing is happening like this.each element in the ndarray is assigned with an index.
# 1(0,0),2(0,1)
# 3(1,0),4(1,1)
# 5(2,0),6(2,1)

# Thus the output is  [1 4 5]

#%%
# ex -2

import numpy as np

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print('The array is:') 
print(x) 
print('\n') 

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols] 
   
print('The corner elements of this array are:') 
print(y)

# The calculation is happening as the previous example.indexing as previous example
# 0     1 	2
# 00	01	02

# 3 	4 	5
# 10	11	12

# 6 	7 	8 
# 20	21	22
	
# 9 	10 	11
# 30	31	32
#%%
# Ex-3

import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print('Our array is:') 
print(x) 
print('\n')  

# slicing 
z = x[1:4,1:3] 

print('Now our array becomes:') 
print(z) 
print('\n')  

# using advanced index for column 
y = x[1:4,[1,2]] 

print('Slicing using advanced indexing for column:') 
print(y)

# The logic is as like rows and colums([1:4,1:3] & 1:4 are rows & 1,2 columns)

#%%
# Boolean Array Indexing

# the resultant object is meant to be the result of Boolean operations, such as comparison operators.

import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print('Our array is:') 
print(x) 
print('\n')  

# Now we will print the items greater than 5 
print('The items greater than 5 are:') 
print(x[x > 5])

#%%

# Compliment Operator(~)
# NaN (Not a Number) elements are omitted by using ~ (complement operator).

import numpy as np
a = np.array([np.nan, 1,2,np.nan,3,4,5]) 
print(a[~np.isnan(a)])





















