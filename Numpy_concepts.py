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

# Strings: 

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

# We can find several built-in container types: lists, dictionaries, sets, and tuples.
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
# Functions : functions are defined using the def keyword

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
# The syntax for defining classes is straightforward

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

#%%
# Numpy : A numpy array is a grid of values, all of the same type, indexed by a 
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
# Create a constant array of 2rows & 2 columns
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
# Slicing: Similar to lists, numpy arrays can be sliced.

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

#%%

# One dimensional slicing and indexing

# Ex1 : slice single item (5) 

import numpy as np 
a = np.arange(10) 
b = a[5] 
print(b)

# ex2 : slice items between indexes,array between 2 and 5,5 not included.

import numpy as np 
a = np.arange(10) 
print(a[2:5])

# ex3
# We can select elements from index 0 to 7 with a step of 2.(stat,stop,step)
import numpy as np 
a = np.arange(10) 
a[:7:2]

# ex4
# We can select elements from index 2 to 7 with a step of 2.(start(2),stop(7),step(2)) 

import numpy as np
a = np.arange(10) 
s = slice(2,7,2) 
print(a[s])

# ex5
# Negetive indexing 
import numpy as np
a = np.arange(10) 
a[::-1]

#%%

# Multidimensional array slicing and indexing

# ex1 : import numpy as np,returns a simple array.

import numpy as np  
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print(a)  

# Output : 
#[[1 2 3]
# [3 4 5]
# [4 5 6]]

# ex2 : we will create an array with the arange functon and reshape it.

import numpy as np
a = np.arange(24).reshape(2,3,4)
a.shape
# output : (2, 3, 4)

print(a)

# output : 

# [[[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
#
# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]]

# The array has 24 elements(0-23),we reshaped it to be a 2-by-3-by-4, three-dimensional array.

# We can visualize this as a two-story building with 12 rooms on each ﬂoor, 3 rows and 4 columns. 

# for selecting a single cell for ex. first floor,first row and first column,we can reoresent it by

print(a[0,0,0]) 
# output : 0    

# If we are not concerned about floor but want 1st row and 1st column ,we replace the first
# index by a colon " :(colon) "

print(a[:,0,0]) 
# output : [ 0 12 ]

print(a[0]) 

# output : 
#[[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

# print(a[0])  == print( a[0, :, :] )== print(a[0, ...]) as an ellipsis replaces multi colons.

# we can find the second floor by

print(a[0,1]) 

# output : [4 5 6 7]

# Ex :  Using steps to slice : we can also select each second element of this selecton.

print(a[0,1,::2]) 
# output : [4 6]  

# Ex : we can use ellipsis to slice  : select rooms on both floors on 2nd column.

print(a[...,1])
 
# output :
#[[ 1  5  9]
# [13 17 21]]

# Both floor 4th column
print(a[...,3])


# Ex : select rooms on both floors on 2nd column.

print(a[:,1]) 

# output :
#[[ 4  5  6  7]
# [16 17 18 19]]

print(a[0,:,1]) 


# Second floor 3rd column
print(a[1,:,2])


# slice items starting from index,first row is sliced.
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print ('Let us slice the array from the index a[1:]')
print(a[1:])


# Normal array created.
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
print (a[1,...])
print('\n')  

# Now we will slice all items from column 1 onwards 
print('The items column 1 onwards are:')
print( a[...,1:])

#%%

# Array in  onedimensional & multidimensional : 
# In a multi-dimensional array, items can be accessed using a comma-separated tuple of indices.

#%%

# onedimensional

import numpy as np

x = np.arange(10)
x
# output : array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# first five elements
x[:5]  
# output :array([0, 1, 2, 3, 4])


# elements after index 5
x[5:]  
# output : array([5, 6, 7, 8, 9])

# middle sub-array
x[4:7]  
# output :array([4, 5, 6])


# middle sub-array
x[4:7]  
# output : array([4, 5, 6])


# every other element, starting at index 1
x[1::2]  
# output : array([1, 3, 5, 7, 9])


# all elements, reversed
x[::-1]  
# output : array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


# reversed every other from index 5
x[5::-2] 
# output: array([5, 3, 1])

#%%
# Multidimensional Array and subarray.

import numpy as np  
a = np.array([[12, 5, 2, 4],[7, 6, 8, 8],[1, 6, 7, 7]]) 
print(a) 
#%%
# Ex1

print(a[0, 0])
# output : 3

print(a[0, 0])
# output : 3

#%%
# Ex2 : two rows, three columns

a[:2, :3]  
 
# output : array([[12,  5,  2],
#               [ 7,  6,  8]])


a[:3, ::2]  # all rows, every other column
# output :array([[12,  2],
#               [ 7,  8],
#               [ 1,  7]])

#%%
# Ex3 : Finally, subarray dimensions can even be reversed together:

x2[::-1, ::-1]

# output : array([[ 7,  7,  6,  1],
#               [ 8,  8,  6,  7],
#               [ 4,  2,  5, 12]])


# Accessing array rows and columns
# This can be done by combining indexing and slicing, using an empty slice marked 
# by a single colon (:):

#%%

# Ex4

# first column of a
print(a[:, 0])
  
# output : [12  7  1]

#%%

# Ex5

# first row of a
print(a[0, :]) 
# output : [12  5  2  4]

# In the case of row access, the empty slice can be omitted for a more compact syntax:

# equivalent to a[0, :]
print(a[0])  
# output : [12  5  2  4]


# Subarrays as no-copy views

#%%
# Ex6

a_sub = a[:2, :2]
print(a_sub)
# output :[[12  5]
#        [ 7  6]]

#%%

# Ex7

# Now if we modify this subarray, we'll see that the original array is changed! Observe

a_sub[0,0] = 99
print(a_sub)

# output :    [[99  5]
#            [ 7  6]]


# Creating copies of arrays : This is done by copy() method.

import numpy as np  
a = np.array([[12, 5, 2, 4],[7, 6, 8, 8],[1, 6, 7, 7]]) 
print(a) 
#%%

# Ex8

a_sub_copy = a[:2,:2].copy()
print(a_sub_copy)

# output : [[12  5]
#           [ 7  6]]


# If we modify the sub array the main array remain untouched.

#%%
# Ex9

a_sub_copy[0, 0] = 42
print(a_sub_copy)

# output : [[12  5]
#            [ 7  6]]
print(a)


# Reshaping arrays : Thisis done using  " reshape " method.

#%%
# Ex10

grid = np.arange(1,10).reshape((3,3))
print(grid)
# output : [[1 2 3]
#           [4 5 6]
#           [7 8 9]]

# Reshaping of Arrays : The common method of reshaping  is by conversion of an one 
# dimensional array into a two dimensional row and column matrix.This can be done by using 
# a "rehape". Another method is by using a "newaxis" keyword within the slicing condition.

#%%

# Ex11

x = np.array([1,2,3])
# row vector via reshape
x.reshape(1,3)
# output : array([[1, 2, 3]])

# row vector via newaxis,the same result as above.
x[np.newaxis, :]
# output : array([[1, 2, 3]])

#%%
# Ex12

# column vector by reshape method.
x.reshape(3,1)
# output :array([[1],
#               [2],
#                [3]])
#%%

# Ex13

# column vector via newaxis
x[:,np.newaxis]
# output :array([[1],
#               [2],
#              [3]])


# Array concartination and splitting.

#%%

# Ex14
x = np.array([1,2,3])
y = np.array([3,2,1])
np.concatenate([x, y])

#%%
# Ex15

# We can also concatenate more than two arrays at once.
 z = np.array([99,99,99])
 np.concatenate([x, y, z])
# output : array([ 1,  2,  3,  3,  2,  1, 99, 99, 99])

# It can also be used for two-dimensional arrays

grid = np.array([[1, 2, 3],[4, 5, 6]])
print(grid)

#%%
# Ex16

# concatenate along the first axis
np.concatenate([grid, grid])

# output:array([[1, 2, 3],
#              [4, 5, 6],
#              [1, 2, 3],
#              [4, 5, 6]])

#%%
# Ex17

# concatenate along the same axis

np.concatenate([grid, grid], axis =1)
# output: array([[1, 2, 3, 1, 2, 3],
#               [4, 5, 6, 4, 5, 6]])

#%%
# Ex18

# For working with mixed dimensional arrays,it can be clearer to use np.vstack(vertical stack) and
# np.hstack for horizontal stack functions.

x = np.array([1,2,3])
grid = np.array([[9,8,7],[6,5,4]])
# vertically stack the arrays
np.vstack([x, grid])

# output: array([[1, 2, 3],
#               [9, 8, 7],
#                [6, 5, 4]])

#%%
# Ex19

# horizontally stack the arrays

y = np.array([[99],[99]])
np.hstack([grid, y])
# output :  array([[ 9,  8,  7, 99],
#                   [ 6,  5,  4, 99]])

# np.dstack will start array along the third axis.

#%%
# Ex20:

a = np.array((1,2,3))
b = np.array((2,3,4))
np.dstack((a,b))
# output : array([[[1, 2],
#                   [2, 3],
#                   [3, 4]]])

#%%
# Splitting of arrays

# The opposite of concatenation is splitting, which is implemented by the 
# functions np.split, np.hsplit, and np.vsplit. For each of these, we can pass a 
# list of indices giving the split points

# Ex21

x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)
# output :

# N split-points, leads to N + 1 subarrays. The related functions np.hsplit and 
# np.vsplit are similar
#%%

# Ex22

grid = np.arange(16).reshape((4, 4))
grid
# output : array([[ 0,  1,  2,  3],
#                 [ 4,  5,  6,  7],
#                  [ 8,  9, 10, 11],
#                  [12, 13, 14, 15]])

#%%
# Ex23

upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

# output :  [[0 1 2 3]
#           [4 5 6 7]]
#           [[ 8  9 10 11]
#            [12 13 14 15]]

#%%
# Ex24

left, right = np.hsplit(grid, [2])
print(left)
print(right)
# output : [[ 0  1]
#           [ 4  5]
#            [ 8  9]
#           [12 13]]
#           [[ 2  3]
#           [ 6  7]
#            [10 11]
#            [14 15]]

# Similarly, np.dsplit will split arrays along the third axis.


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
# Here the indexing is happening like this.each element in the ndarray is assigned with an index.
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

# output: [1. 2. 3. 4. 5.]

#%%
# How to filter out the non-complex elements from an array.

import numpy as np 
a = np.array([1, 2+6j, 5, 3.5+5j]) 
print(a[np.iscomplex(a)])

# output: [2. +6.j 3.5+5.j]

#%%
# Broadcasting : numpy.broadcast

# Broadcasting provides a means of vectorizing array operations so that looping occurs in C 
# instead of Python

# When operating on two arrays, NumPy compares their shapes element-wise. It starts with the
# trailing dimensions, and works its way forward. Two dimensions are compatible when
# they are equal, or
# one of them is 1.

import numpy as np 
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0]) 
print(a + b)

# output : 
#    [[ 1.  2.  3.]
#     [11. 12. 13.]
#     [21. 22. 23.]
#     [31. 32. 33.]]


#%%
# Iterating Over Array :  nditer

# numpy  has " numpy.nditer " a multidimensional iterator object using which we cam iterate over 
# an array.n

#%%

# Ex:

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print(a)

# output :[[ 0 5 10 15]
#       [20 25 30 35]
#       [40 45 50 55]]

# Now  let's use the iterator and see the reult

for x in np.nditer(a):
   print(x)

# output : 
#   0
#   5
#   10
#   15
#   20
#   25
#   30
#   35
#   40
#   45
#   50
#   55

#%%
   
# Ex:

# Let's check the impact on an array and its transpose,impact of "nditer"   on it.

# An array
   
import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 
print(a)


# output : [[ 0  5 10 15]
#           [20 25 30 35]
#           [40 45 50 55]]

# Transpose of the array :

b = a.T 
print(b)

# output : [[ 0 20 40]
#           [ 5 25 45]
#           [10 30 50]
#           [15 35 55]]

# apply "nditer" on 'b'

for x in np.nditer(b): 
   print(x)
   
# output :
#   0
#   5
#   10
#   15
#   20
#   25
#   30
#   35
#   40
#   45
#   50
#   55

#%%
# Iteration Order : C-style order & F-style order

# C-style order
   
# The iterated array can be Sorted in C-style order & F-style order which is 
# more efficient way of iterating over an array.
   
c = b.copy(order = 'C')   
print(c)

# output : 
#   [[ 0 20 40]
#   [ 5 25 45]
#   [10 30 50]
#   [15 35 55]]

for x in np.nditer(c):
   print(x)
   
# output : 
#   0
#   20
#   40
#   5
#   25
#   45
#   10
#   30
#   50
#   15
#   35
#   55   
   
#%%
#  F-style order
   
c = b.copy(order = 'F')
print(c)

# output : 
#   [[ 0 20 40]
#    [ 5 25 45]
#    [10 30 50]
#   [15 35 55]]

for x in np.nditer(c):
   print(x)

# output :    
#   0
#   5
#   10
#   15
#   20
#   25
#   30
#   35
#   40
#   45
#   50
#   55
   
#%%

# Let's check an nditer object and use order by:
   
a = np.arange(0,60,5) 
a = a.reshape(3,4)   
print(a) 

# output : 
#       [[ 0  5 10 15]
#       [20 25 30 35]
#       [40 45 50 55]]

# C-style order

for x in np.nditer(a, order = 'C'): 
   print(x)

# output :
#   0
#   5
#   10
#   15
#   20
#   25
#   30
#   35
#   40
#   45
#   50
#   55   
   
# F-style order

for x in np.nditer(a, order = 'F'): 
   print(x)

# output :
   
#   0
#   20
#   40
#   5
#   25
#   45
#   10
#   30
#   50
#   15
#   35
#   55

#%%
# Modifying Array Values:
   
#%%   

# op_flags in nditer which enable modifying array elements  into read-only,
# read-write or write-only mode  .
   
a = np.arange(0,60,5) 
a = a.reshape(3,4)   
print(a) 

# output : 
#       [[ 0  5 10 15]
#       [20 25 30 35]
#       [40 45 50 55]]

# now wewill use op_flag on it(multiplied by 2)

for x in np.nditer(a, op_flags = ['readwrite']):
   x[...] = 2*x
   
print(a)

# output :  [[  0  20  40  60]
#           [ 80 100 120 140]
#           [160 180 200 220]]

#%%
# External Loop

#%%
#  "nditer" has  ‘flags’ parameter where each column is traversed(sideways) by the iterator.

a = np.arange(0,60,5) 
a = a.reshape(3,4)   
print(a) 

# output : 
#       [[ 0  5 10 15]
#       [20 25 30 35]
#       [40 45 50 55]]

# Now apply "flags"

for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print(x)

# output : 
#   [  0  80 160]
#   [ 20 100 180]
#   [ 40 120 200]
#   [ 60 140 220]

#%%
# Broadcasting Iteration

#%%

# an array a has dimension 3X4, and there is another array b of dimension 1X4,
# the iterator of following type is used (array b is broadcast to size of a).
   
a = np.arange(0,60,5) 
a = a.reshape(3,4)   
print(a) 

# output : 
#       [[ 0  5 10 15]
#       [20 25 30 35]
#       [40 45 50 55]]

# Second Array

b = np.array([1, 2, 3, 4], dtype = int) 
print(b) 

# output : [1 2 3 4]

# Modified

for x,y in np.nditer([a,b]): 
   print("%d:%d" % (x,y))

# output :
#   0:1
#   20:2
#   40:3
#   60:4
#   80:1
#   100:2
#   120:3
#   140:4
#   160:1
#   180:2
#   200:3
#   220:4

#%%
# Array Manipulation : Routines availabe for array manupulation are 

#%%

# For Changing Shape :
   
# reshape : a.reshape()
   
# a.reshape(), then apply a.flat[]
   
# a = np.arange().reshape() > a.flatten() > a.flatten(order = 'F')(Ordering)
   
# a = np.arange().reshape() > a.ravel() > a.ravel(order = 'F')(Ordering)
   
#%%
   
# For Transpose Operations :
   
# a = np.arange().reshape() > np.transpose(a)
   
# a = np.arange().reshape() > a.T
       
# rollaxis :

# a 3d ndarray 
   
import numpy as np 
a = np.arange(8).reshape(2,2,2) 
print( a )
print ('\n')
# to roll axis-2 to axis-0 (along width to along depth) 

# now we will use rollaxis function
print (np.rollaxis(a,2))  
# to roll axis 0 to 1 (along width to height) 
print('\n' )

print('After applying rollaxis function:' )
print (np.rollaxis(a,2,1))

# output:
#   [[[0 2]
#     [1 3]]
#
#   [[4 6]
#    [5 7]]]


# swapaxes

import numpy as np 
a = np.arange(8).reshape(2,2,2) 
print( a )
print ('\n')  
# now swap numbers between axis 0 (along depth) and axis 2 (along width) 

print 'after applying the swapaxes function:' 
print np.swapaxes(a, 2, 0)

#%%

# Changing Dimensions :

# broadcast
# Produces an object that mimics broadcasting

# broadcast_to
# Broadcasts an array to a new shape

# expand_dims
# Expands the shape of an array

# squeeze
# Removes single-dimensional entries from the shape of an array

#%%

# Joining Arrays

# concatenate
# Joins a sequence of arrays along an existing axis

# stack
# Joins a sequence of arrays along a new axis

# hstack
# Stacks arrays in sequence horizontally (column wise)

# vstack
# Stacks arrays in sequence vertically (row wise)

#%%

# Splitting Arrays

# split
# Splits an array into multiple sub-arrays
#
# hsplit
# Splits an array into multiple sub-arrays horizontally (column-wise)
#
# vsplit
# Splits an array into multiple sub-arrays vertically (row-wise)

#%%

# Adding / Removing Elements

# resize
# Returns a new array with the specified shape

# append
# Appends values to the end of an array

# insert
# Inserts the values along the given axis before the given indices

# delete
# Returns a new array with sub-arrays along an axis deleted

# unique
# Finds the unique elements of an array

#%%

# Binary Operators:  np.bitwise_and()

import numpy as np
a,b = 13,17
print(bin(a),bin(b))
np.bitwise_and(13,17)

# output : 1
# =============================================================================
# String Functions
# =============================================================================
# Concatenation 

# two strings:

import numpy as np
print(np.char.add(['abc'],['xyz']))
print(np.char.add(['a,b,c'],['x,y,z']))

print(np.char.add(['Good','Morning'], ['xyz' , 'abc']))

# output : ['Goodxyz' 'Morningabc']

#%%
# Multiply : np.char.multiply

import numpya s np
print(np.char.multiply('hello',3))

# output : hellohellohello

#%%
# center : numpy.char.center()

import numpy as np
print(np.char.center( 'Morning', 30, fillchar = '+'))

# output : +++++++++++Morning++++++++++++ (30char including string)

#%%
# capitalize : numpy.char.capitalize()

import numpy as np
print(np.char.capitalize('good morning'))

# output : Good morning

#%%
# title : numpy.char.title()
import numpy as np
print(np.char.title('good morning Aryan'))

# output : Good Morning Aryan

#%%
# lower : numpy.char.lower()
import numpy as np
print(np.char.lower('GOOD MORNING ARYAN'))

# output : good morning aryan

#%%
# upper : numpy.char.upper()
import numpy as np
print(np.char.upper('good morning aryan'))

# output : GOOD MORNING ARYAN

#%%
# split :  numpy.char.split()

import numpy as np
print(np.char.split('good morning aryan'))

# output : 
['good', 'morning', 'aryan']

#%%
# join : numpy.char.join()

import numpy as np
print(np.char.join(':','dmy')) 
print(np.char.join([':','-'],['dmy','ymd']))

# output : d:m:y , ['d:m:y' 'y-m-d']

#%%
# replace : numpy.char.replace()

import numpy as np 
print(np.char.replace ('Good morning arab', 'arab', 'Aryan'))

# output : Good morning Aryan

# =============================================================================
# Mathematical Functions
# =============================================================================

# NumPy provides standard trigonometric functions, functions for arithmetic operations, 
# handling complex numbers, etc.

#%%

# Trigonometric Functions:

# We will now take an array,convert it to radians(multiply with pi/180),the find sin,cos & tan values.
#%%
# Ex:1

import numpy as np 
a = np.array([0,30,45,60,90]) 


# multiply with pi/180 to convert to radians  and finding sin value.

print ('Sine of different angles:' )
print(np.sin(a*np.pi/180)) 
print ('\n' ) 

#[-0.02966624  0.02617695 -0.00349065  0.01047178  0.17364818]


# calculating the cosine value of angles

print( 'Cosine values for angles in array:') 
print (np.cos(a*np.pi/180)) 
print ('\n')  

# output : [0.99955986 0.99965732 0.99999391 0.99994517 0.98480775]

# calculating the tangent value of angles

print('Tangent values for given angles:') 
print (np.tan(a*np.pi/180))

# output : [-0.02967931  0.02618592 -0.00349067  0.01047236  0.17632698]

# "arcsin", "arcos", and "arctan" functions return the trigonometric 
# inverse of sin, cos, and tan of the given angle.
#%%
# Ex:2

import numpy as np 
a = np.array([0,30,45,60,90]) 

print('sine values are :') 
sin = np.sin(a*np.pi/180) 
print(sin)
print('\n')  

# output: [0.         0.5        0.70710678 0.8660254  1.        ]

#%%
# Ex:3

print ('sine inverse of angles, values in radians.')
inv = np.arcsin(sin) 
print (inv)
print ('\n')  
 
# output:

# sine inverse of angles. Returned values are in radians.
# [0.         0.52359878 0.78539816 1.04719755 1.57079633]

#%%
# Ex:4

print('Check result by converting to degrees:') 
print (np.degrees(inv)) 
print('\n')  

# output: [ 0. 30. 45. 60. 90.]

#%%
# Ex:5

print('arccos and arctan functions behave similarly:' )
cos = (np.cos(a*np.pi/180) )
print (cos )
print ('\n')

# output:  [ 0.9998477   0.99531218 -0.54463904  0.99995103  0.9023447 ]

#%%
# Ex:6

print ('Inverse of cos:') 
inv = (np.arccos(cos) )
print (inv )
print ('\n')

# output:  [0.01745329 0.09686577 2.14675498 0.00989602 0.44561746]

#%%
# Ex:7
# output:

print ('In degrees:') 
print (np.degrees(inv)) 
print ('\n')
#%%
# Ex:8

print ('Tan function:') 
tan = (np.tan(a*np.pi/180)) 
print (tan)
print ('\n')

# output: [ 0.01745506  0.09716988 -1.53986496  0.00989634  0.47766128]

#%%
# Ex:9

print ('Inverse of tan:') 
inv = (np.arctan(tan))
print (inv)
print ('\n') 

# output: [ 0.01745329  0.09686577 -0.99483767  0.00989602  0.44561746]

#%%
# Ex:10

print('In degrees:')
print( np.degrees(inv) )

# output:[  1.      5.55  -57.      0.567  25.532]

#%%
# Rounding Functions:

#%%

# numpy.around() : 

# EX :

import numpy as np 
a = np.array([1.0,5.55, 123, 0.567, 25.532]) 

print ('Original array:')
print (a)
print ('\n')  

print ('After rounding:')
print (np.around(a) )
print (np.around(a, decimals = 1))
print (np.around(a, decimals = -1))

#%%
# numpy.floor()

# The floor of the scalar x is the largest integer i, such that i <= x. 
# flooring is always rounding away from "0"
# EX :

import numpy as np 
a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 

print ('The given array:' )
print( a) 
print ('\n')  
+
print('The modified array:') 
print (np.floor(a))

# Output : [-2.  1. -1.  0. 10.]

#%%
# numpy.ceil()

# EX :

import numpy as np 
a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 

print ('The given array:' )
print( a )
print ('\n')  

print ('The modified array:') 
print (np.ceil(a))

#  Output : [-1.  2. -0.  1. 10.]

# =============================================================================
# Arithmetic Operations : add(), subtract(), multiply(), and divide()
# =============================================================================

# EX :1

import numpy as np 
a = np.arange(9, dtype = np.float_).reshape(3,3) 

print('Array 1:') 
print (a) 
print ('\n')  

# output :Array 1:
#   [[0. 1. 2.]
#    [3. 4. 5.]
#   [6. 7. 8.]]


# EX :2

print('Second array:') 
b = np.array([10,10,10]) 
print( b )
print('\n')  

# output :Second array:
#       [10 10 10]

# EX :3

print ('Add the two arrays:') 
print (np.add(a,b))
print ('\n')

# output :Add the two arrays:
#   [[10. 11. 12.]
#    [13. 14. 15.]
#    [16. 17. 18.]]

# EX :4

print('Subtract the two arrays:') 
print(np.subtract(a,b)) 
print('\n')  

# output :


# EX :5

print('Multiply the two arrays:') 
print(np.multiply(a,b))
print('\n')

# output :

#   [[ 0. 10. 20.]
#    [30. 40. 50.]
#   [60. 70. 80.]]


# EX :6

print('Divide the two arrays:') 
print(np.divide(a,b))

# output :

# [[0.  0.1 0.2]
# [0.3 0.4 0.5]
# [0.6 0.7 0.8]]

# =============================================================================
# Statistical function 
# =============================================================================
# statistical functions for finding minimum, maximum, percentile standard deviation and variance, etc.

#%%

# ex:

import numpy as np
a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print(a)

# output: 

# [[3 7 5]
# [8 4 3]
# [2 4 9]]

# we will now apply a.min() function on the array to find min no in the array.

# will print amin() on axis 1(column)
print(np.amin(a, 1))

# output: [0 2]

# will print amin() on axis 0(row)
print(np.amin(a,0))
 
# output: [0 1]

# applying amax() function
print(np.amax(a)) 

# output : 3

# applying amax() function on rows.
print(np.amax(a, axis = 0))

# output : [2 3]

#%%

# numpy.ptp() : Gives range of values (maximum - minimum) of values along an axis.

import numpy as np
a = np.array([[3,7,5],[8,4,3],[2,4,9]])  
print(a)

# output: 

# [[3 7 5]
# [8 4 3]
# [2 4 9]]

print(np.amin(a, axis=0)) 
# output : [2 4 3] (across all rows)

print(np.amin(a, axis=1)) 
# output : [3 3 2] (across all columns)
  

# we will apply  ptp() on a.
print(np.ptp(a))

# output:7
 
# we will apply ptp() along axis 1
print(np.ptp(a, axis = 1))   

# output: [4 5 7] (maximum - minimum across all the elements in all columns)

#%%
# Percentile : numpy.percentile()

import numpy as np
a = np.array(([[30,40,70],[80,20,10],[50,90,60]]))
print(a)

# output:

#[[30 40 70]
# [80 20 10]
# [50 90 60]]

# now we will be Applying percentile() function on "a" 
print(np.percentile(a,50))
# output: 50

# Now we will apply percentile() function along axis 1
print(np.percentile(a,50, axis = 1)) 
# output: [40. 20. 60.]

# Now we will apply percentile() function along axis 0
print(np.percentile(a,50, axis = 0))
# output: [50. 40. 60.]

#%%

# Mean : numpy.mean()

import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print(a)

# now we will calculate the mean acros the array.
print(np.mean(a))

# output : 3.6666666666666665

# Now we will apply mean() function along axis 1
print(np.mean(a, axis = 1)) 
# output: [2. 4. 5.]

# Now we will apply mean() function along axis 0
print(np.mean(a, axis = 0))
# output: [2.66666667 3.66666667 4.66666667]

#%%
# Average : numpy.average()

# It computes the weighted average of elements in an array according to their respective
# weight given in another array.

import numpy as np 
a = np.array([1,2,3,4])
print(a)

# Now we will apply np.average() on "a"
print(np.average(a))
# output : 2.5

# now we will define a weight and then will calculate.
wts = np.array([4,3,2,1]) 

# we will apply the average function again
print(np.average(a,weights = wts)) 
# output : 2.0

# we will calculate the sum of weights.
print(np.average([1,2,3, 4],weights = [4,3,2,1], returned = True))

# output : (2.0, 10.0)

#%%
# Standard deviation :  std = sqrt(mean(abs(x - x.mean())**2))
# in numpy we use np.std[] & variance : np.var()

# Ex :

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a)

# calculate standard deviation 
print(np.std(a))
# Output: 2.581988897471611
print(np.var(a))
# output : 6.666666666666667

# =============================================================================
# Sort, Search & Counting Functions : sorting algorithm .
# =============================================================================

 
numpy.sort : umpy.sort(a, axis, kind, order)
  
# Ex:
  
import numpy as np
a = np.array([[1,8,9],[5,3,4]])
print(a)

# output :
#   [[1 8 9]
#   [5 3 4]]

# Applyting sort () function

print(np.sort(a))


# output : [[1 8 9]
#            [3 4 5]]

# sorting along the axis 0

print(np.sort(a, axis = 0))

# output :   [[1 3 4]
#            [5 8 9]]


# sorting along the axis 1

print(np.sort(a, axis = 1))

# output :  [[1 8 9]
#            [3 4 5]]

# Ex : 2

# we will use order parametrer in sort function

dt = np.dtype([('name', 'S10'),('age', int)]) 
a = np.array([("Aryan",21),("Roney",25),("Parth", 17), ("Sweety",27)], dtype = dt) 
print(a)

# output : [(b'Aryan', 21) (b'Roney', 25) (b'Parth', 17) (b'Sweety', 27)]

# now we will order by name

print(np.sort(a, order = 'name'))

# output : [(b'Aryan', 21) (b'Parth', 17) (b'Roney', 25) (b'Sweety', 27)]

#%%

# numpy.argsort() : indirect way of sorting the array

# Ex:

import numpy as np 
x = np.array([3, 1, 2]) 
print (x )

# We will apply  np.argsort() function
y = np.argsort(x) 
print(y) 

# output : [1 2 0]

# we willReconstruct the original array using loop.

for i in y: 
   print(x[i])
   
# output :   
1
2
3

#%%

# numpy.lexsort()

# This performs an indirect sorting using a sequence of keys.

a = ('Aryan','Parth','Roney','Sweety')
b = ('a.y.','a.y.','b.y.','b.y.')

array1 = np.lexsort((a,b))
print(array1)

# we will use this index to get sorted data
print( [a[i] + ", " + b[i] for i in array1])

# output : ['Aryan, a.y.', 'Parth, a.y.', 'Roney, b.y.', 'Sweety, b.y.']

#%%
# numpy.argmax() and numpy.argmin() : returns a minimum and maximum element respectively 
# along the axis.

# Ex:

import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 
print(a) 
# output :
#   [[30 40 70]
#   [80 20 10]
#   [50 90 60]]


# output :Apply argmax() function
print(np.argmax(a)) 
# output : 7


# output :print 'Index of maximum number in flattened array' 
print(a.flatten()) 
# output : [30 40 70 80 20 10 50 90 60]


# output :print 'Array containing indices of maximum along axis 0:' 
maxindex = np.argmax(a, axis = 0) 
print(maxindex) 
# output : [1 2 0]

# output :print 'Array containing indices of maximum along axis 1:' 
maxindex = np.argmax(a, axis = 1) 
print(maxindex) 
# output : [2 0 1]


# output :print 'Applying argmin() function:' 
minindex = np.argmin(a) 
print(minindex) 
# output : 5
   
# output :print 'Flattened array:' 
print(a.flatten()[minindex]) 
# output : 10

# output :print 'Flattened array along axis 0:' 
minindex = np.argmin(a, axis = 0) 
print(minindex)
# output : [0 1 1]

# output :print 'Flattened array along axis 1:' 
minindex = np.argmin(a, axis = 1) 
print(minindex)
# output : [0 2 0]

#%%
# numpy.nonzero() : returns the indices of non-zero elements in the input array.

# Ex:

import numpy as np 
a = np.array([[30,40,0],[0,20,10],[50,0,60]])
print(a)
# output : [[30 40  0]
#           [ 0 20 10]
#           [50  0 60]]

# we will apply nonzero function to it

print(np.nonzero(a))

# output : (array([0, 0, 1, 1, 2, 2], dtype=int64), array([0, 1, 1, 2, 0, 2], dtype=int64))

#%%

# numpy.where :

import numpy as np
a = np.arange(9.).reshape(3,3)
print(a)

# output :
#   [[0. 1. 2.]
#    [3. 4. 5.]
#    [6. 7. 8.]]

# we will apply the wehere function here
x = np.where(a > 3) 
print(x)  
# output : (array([1, 1, 2, 2, 2], dtype=int64), array([1, 2, 0, 1, 2], dtype=int64))

# we will apply 'x' on 'a'
print(a[x])
# output : [4. 5. 6. 7. 8.]

#%%

# numpy.extract() : Returns the value against certain condition.

import numpy as np
a = np.arange(9.).reshape(3,3)
print(a)

# now we will apply the condition on which the calculation will happen.

condition = np.mod(a,2) == 0
print(condition)
# output:
#   [[ True False  True]
#   [False  True False]
#    [ True False  True]]


# now we will apply 'condition' on 'a'

print(np.extract(condition, a))

# output : [0. 2. 4. 6. 8.]

# =============================================================================
# Copies & Views :
# =============================================================================
# Copies : When the contents are physically stored in another location, it is called Copy.
# Views : a different view of the same memory content is provided, we call it as View.

# No Copy :

import numpy as np
a = np.arange(6)
print(a)
# output : [0 1 2 3 4 5]

# applying the id() function on "a"
print(id(a))
# output :123121136

# now we will define b = a
b = a
print(b)
# output :[[0 1]
#       [2 3]
#       [4 5]]

# we will apply id() function on b and we willm see the output same as "a"
print(id(b))
# output : 123121136

# check the shpae of b
b.shape = 3,2
print(b)
# output :
#   [[0 1]
#    [2 3]
#    [4 5]]

print(a)
# output :[[0 1]
#         [2 3]
#         [4 5]]

#%%
# View or Shallow Copy

# A new array object that looks at the same data of the original array. 
# Change in dimensions of the new # array doesn’t change dimensions of the original.

import numpy as np
a = np.arange(6).reshape(3,2)
print(a)
# output : [[0 1]
#           [2 3]
#           [4 5]]


# now we will create a view of "a"
b = a.view()
print(b)
# output :[[0 1]
#        [2 3]
#        [4 5]]

# we will check the id of both "a" & "b"
print(id(a))
# output : 154624208
print(id(b))
# output : 154627008


# we will change the shape of "b" which will never change the shape of "a"
b.shape = 2,3 
print(b)
# output :[[0 1 2]
#        [3 4 5]]

print(a)
# output :
#   [[0 1]
#    [2 3]
#    [4 5]]

#%%
# Deep Copy
# ndarray.copy() function creates a deep copy.which is a complete copy of array and its data.

import numpy as np 
a = np.array([[10,10], [2,3], [4,5]])  
print(a)  
# output :
#   [[10 10]
#    [ 2  3]
#    [ 4  5]]

# Create a deep copy of a.
b = a.copy() 
print(b) 
# output :
#   [[10 10]
#    [ 2  3]
#    [ 4  5]]

# "b" does not share any memory of a 
print('Can we write b is a') 
print(b is a)  
# output :Can we write b is a
#          False


# 'Change the contents of b:' 
b[0,0] = 100 

print('Modified array b:') 
print(b)  
# output :
#       [[100  10]
#        [  2   3]
#       [  4   5]]


# "a" remains unchanged.
print(a)
# output :[[10 10]
#        [ 2  3]
#        [ 4  5]]

# =============================================================================
# Matrix Library: 
# =============================================================================

# numpy.matlib : this module returns matrices instead of ndarrays.


# Matrix library (numpy.matlib)
# With the following replacement functions that return matrices instead of ndarrays.

# Functions that are also in the numpy namespace and return matrices :

# np.mat('1 1; 1 1') > Interpret the input as a matrix.

# np.matrix('1 2; 3 4') >  Returns a matrix from an array-like object, or from a string of data.

# np.asmatrix(x),x = input  > Interpret the input as a matrix.

# np.bmat([[A, B], [C, D]]) (define A,B,C,D)  > Build a matrix object from a string,
# nested sequence, or array.

# Replacement functions in matlib : Ex:
# Ex : np.matlib.empty((2, 2)) :  Returns a new matrix of given shape and type, 
# without initializing entries.
# Ex: np.matlib.empty((2, 2), dtype=int)

# Ex: np.matlib.zeros((2, 3)) :  Returns a matrix of given shape and type, filled with zeros.

# Ex: np.matlib.ones((2,3)) : Matrix of ones.

# Ex: np.matlib.eye(3, k=1, dtype=float) : Returns a matrix with ones on the diagonal 
# and zeros elsewhere.

# Ex: np.matlib.identity(3, dtype=int) :  Returns the square identity matrix of given size.

# Ex : Define : a0 = np.array(1)
#       np.matlib.repmat(a0, 2, 3) :  Repeat a 0-D to 2-D array or matrix MxN times.
# Ex:   a1 = np.arange(4)
#        np.matlib.repmat(a1, 2, 2)

# Ex: np.matlib.rand(2, 3)  : Returns a matrix of random values with given shape.
#      np.matlib.rand((2, 3))
#      np.matlib.rand((2, 3), 4)

# ex: np.matlib.randn(*args) returns a random matrix with data from the “standard normal”
# distribution.(see example in #numpy.matlib.randn )

# =============================================================================
# Linear Algebra
# =============================================================================
# np.dot

# dot product of two arrays.
# for 2-D array it's matrix multplication.
# for 1-D, it is inner product of vectors.
# for n dimensional it is a sum product over the last axis of a and the second-last axis of b.

# Ex:

import numpy.matlib 
import numpy as np 
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
np.dot(a,b)

# output:
# array([[37, 40],
#       [85, 92]])

# The calculation will be as follows
(1*11+2*13,1*12+2*14),(3*11+4*13, 3*12+4*14)

#%%
# np.vdot()

# It is the dot product of two vectors.if ist argument is complex then the 
# conjugate is used for the calculation.If argument is multidimensiinal then calculation is flatten.
# 

import numpy.matlib 
import numpy as np 
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
print(np.vdot(a,b)) 


# output: 130

# The calculation : 1*11+2*12+3*13+4*14

#%%

# np.innner() : Inner product of two array.
import numpy.matlib 
import numpy as np 
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
print(np.inner(a,b)) 

# The calculation is done as (1*11+2*12, 1*13+2*14 
#                            3*11+4*12, 3*13+4*14 )

#%%
# np.matmul() : Matrix product of two arrays

# we can do the matrix multiplication for 2d array,2d mixed with 1d etc.

#%%
# determinant : numpy.linalg.det()

# Computes the determinant of the array

#%%
# solve : numpy.linalg.solve() 

# Solves the linear matrix equation

# inv : numpy.linalg.inv()

# Finds the multiplicative inverse of the matrix

# =============================================================================
# MATPLOTLIB
# =============================================================================

# This is the plotting library for python.
# It is used along with NumPy to provide an environment that is an effective open 
# source alternative for MatLab.
# from matplotlib import pyplot as plt
# for plotting 2-D arrays use pyplot(). function.

#%%
# Ex: pyplot

import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11) 
y = 2 * x + 5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y,"or") 
plt.show()

#%%
# Ex : sinewave plot

import numpy as np 
import matplotlib.pyplot as plt  

# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 
plt.title("sine wave form") 

# Plot the points using matplotlib 
plt.plot(x, y,"or") 
plt.show() 

#%%
# Ex2 : sinewave equation A sin(wt),A = amplitude, w = Frequency,t = time

import numpy as np
import matplotlib.pyplot as plt
# get x value 
x = np.arange(0, 10, 0.1);
# amplitude of sine wave is sine(time)
y = np.sin(x)
# we will plot a sine wave for the amplitude and time
plt.plot(x,y,"vm")
# title of the sine wave 
plt.title('Sine wave Time vs Amplitude')
plt.show()

#%%

# Ex3 : sub plot(plot different things in same figure)

import numpy as np
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on sine and cosine curves 
x = np.arange(0, 3 * np.pi, 0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x) 

# Set up a subplot grid that has height 2 and width 1, 
# and set the first such subplot as active. 
plt.subplot(2, 1, 1)
   
# Make the first plot 
plt.plot(x, y_sin,"r") 
plt.title('Sine')  
   
# Set the second subplot as active, and make the second plot. 
plt.subplot(2, 1, 2) 
plt.plot(x, y_cos,"m") 
plt.title('Cosine')  
   
# Show the figure. 
plt.show()

#%%
# bar() : for generating bar graphs

from matplotlib import pyplot as plt
x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.bar(x,y, align = 'center')
plt.bar(x2,y2, color = 'r', align = 'center')
plt.title("Bar Graph")
plt.ylabel('Y axis') 
plt.xlabel('X axis')  
plt.show()


# =============================================================================
# Histogram :
# =============================================================================
# numpy.histogram() takes input array an bins as the two parametres.
# alha for the opacity of the graph.
# 

Ex :

import numpy as np    
from matplotlib import pyplot as plt
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a, bins =[20,40,60,80,100],ec='red')
plt.title("Histogram")
plt.show()

# Ex:

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand((100)) 
bins = np.linspace(0, 2, 30)
plt.title('Relative Amplitude',fontsize=10)
plt.xlabel('Random Histogram')
plt.ylabel('Frequency',fontsize=10)
plt.hist(x, bins, alpha= 0.7, histtype='bar', color = 'r', ec='b')

plt.legend(loc='upper right',fontsize=10)
plt.xticks(fontsize = 10) 
plt.yticks(fontsize = 10) 
plt.show()

# =============================================================================
# I/O with numpy 
# =============================================================================
# load() & save() functions with numpy extensions that takes care about the binary files.
# loadtxt() and savetxt() handales text files.

#%%
# numpy.save()

import numpy as np 
a = np.array([1,2,3,4,5]) 
np.save('outfile',a)

# to reconstruct an array from the "outfile.npy" we will use load() function.
import numpy as np 
b = np.load('outfile.npy') 
print(b) 
# =============================================================================
# savetxt()
# =============================================================================
# It uses savetxt() and loadtxt() for saving and loading 

import numpy as np 

a = np.array([1,2,3,4,5]) 
np.savetxt('out.txt',a) 
b = np.loadtxt('out.txt') 
print(b) 