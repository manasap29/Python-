
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('reset', '-f')
#https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt


# In[ ]:


# Q-1 Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).


# In[ ]:


# 1 
for i in range(2000,3200):
    if i % 7 == 0 and i % 5!=0:
        print(i)


# In[ ]:


# 2         
num = list(range(2000,3200))
num = filter(lambda x : x % 7 == 0 and  x % 5 != 0, num)
num = list(num)
print(num)


# In[ ]:


#3
print(list(filter(lambda x: x%7 == 0 and x%5 !=0, list(range(2000,3200)))))        


# In[ ]:


#Q-2 Write a Python program to print out all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
#
# Sample numbers list:
#
# numbers = [    
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#    958,743, 527
#    ]


# In[ ]:


numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
          ]

numbers1 = [i for i in numbers if i%2 == 0 and i <= 237] 
numbers1


# In[ ]:


# Q-3   Write a program which can compute the factorial of a given numbers.
#    The results should be printed in a comma-separated sequence on a single line.
#    Suppose the following input is supplied to the program:
#    8
#    Then, the output should be:
#    40320


# In[ ]:


fact = lambda x : 1 if x == 0 and 1 else x * fact(x-1)
fact(int(input()))


# In[ ]:


#    Q-4
#    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#    Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#    Example
#    Suppose the following inputs are given to the program:
#    3,5
#    Then, the output of the program should be:
#    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 


# In[ ]:


row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)


# In[ ]:


# Q-5
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number
# between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program:
#8 Then, the output should be:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


# In[ ]:


d = dict()
for i in range(1,i):
    d[i] = i**2
print(d)


# In[ ]:


values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


# In[ ]:


# Q:6
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains 
# every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98


# In[ ]:


import numpy as np
values = input("comma separated numbers : ")
l = values.split(",")
print('list :', l)


# In[ ]:


tup = tuple(l)
print(tup)


# In[ ]:


lst = [1,2,3,4,5,6]
tup = tuple(lst)
print(tup)


# In[ ]:


# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters


# In[ ]:


class IOString():
    def _init_(self):
        self.str1 = ""
        
    def get_String(self):
        self.str1 = input()
        
    def print_String(self):
        print(self.str1.upper())
        
str1 = IOString()
str1.get_String()
str1.print_String()        


# In[ ]:


# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24


# In[ ]:


C = 50
H = 30
Q = Square root of [(2 * C * D)/H]


# In[ ]:


import math
import numpy as np
D = np.array([[int(i) for i in input().split(",")]])
C = 50
H = 30
Q = np.sqrt([(2*C*D)/H]).round()


# In[ ]:


Q


# In[ ]:


# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world


# In[ ]:


lst = input().split(',')
lst.sort()
print(",".join(lst))


# In[ ]:


# Question:
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# # 


# In[ ]:


def capital():
  lines = []
  while True:
    l = input()
    if l:
      lines.append(l.upper())
    else:
      break
  for sentence in lines:
    print (sentence)

capital()


# In[ ]:


lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)


# In[ ]:


# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world


# In[ ]:


x = sorted(list(set(input().split()))) 
print(" ".join(x))


# In[ ]:


x = input().split()
for i in x:
    if x.count(i) >1:
        x.remove(i)
x.sort()
print(" ".join(x))


# In[ ]:


# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.


# In[ ]:


def check(x):
    return int(x,2)%5 == 0
data = input().split(',')
data = list(filter(check,data))
print(",".join(data))


# In[ ]:


data = input().split(',')
data = list(filter(lambda i:int(i,2)%5==0,data))    
print(",".join(data))


# In[ ]:


# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# In[ ]:


lst = [str(i) for i in range(1000,3000)]
lst = list(filter(lambda i : all(ord(j)%2 == 0 for j in i),lst))
print(",".join(lst))


# In[ ]:


def check(number):
    return all(ord(i)%2 == 0 for i in number)
lst = [str(i) for i in range(1000,3001)] 
lst = list(filter(check,lst))
print(",".join(lst))


# In[ ]:


# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


# In[ ]:


x = input()
count_letter = 0
count_digit = 0
for i in range(len(x)):
    if x[i].isalpha():
        count_letter+= 1
    if x[i].isdigit():
        count_digit+= 1
print(count_letter)
print(count_digit)
    


# In[3]:


x = input()
count_letter = 0
count_digit = 0

for i in x:
    count_letter+=i.isalpha()
    count_digit+=i.isnumeric() 
print("%d %d" %(count_letter,count_digit))


# In[8]:


# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9


# In[14]:


x = input()
upper = 0
lower = 0

for i in x:
    lower+=i.islower()
    upper+=i.isupper()
print("%d %d" %(upper,lower))


# In[ ]:


# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# In[18]:


a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total)


# In[ ]:




