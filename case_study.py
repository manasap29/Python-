
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
    


# In[ ]:


x = input()
count_letter = 0
count_digit = 0

for i in x:
    count_letter+=i.isalpha()
    count_digit+=i.isnumeric() 
print("%d %d" %(count_letter,count_digit))


# In[ ]:


# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9


# In[ ]:


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


# In[ ]:


a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total)


# In[ ]:


# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# In[ ]:


list = [i for i in input().split(',') if int(i)% 2 != 0]
print(list)         


# In[ ]:


# list = input().split(',')
# list = list(filter(lambda i :i%2!=0, list))
# list


# In[ ]:


# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# In[ ]:


class Account:
    def __init__(self,myaccount,balance):
        self.myaccount = myaccount
        self.balance = balance
     
    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print('Amount Deposited ')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')   


# In[ ]:


acct  = Account('Aryan',0)


# In[ ]:


acct.deposit(300)


# In[ ]:


acct.deposit(300)


# In[ ]:


acct.withdraw(200)


# In[ ]:


acct.deposit(100)


# In[ ]:


acct.balance


# In[ ]:


# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# In[ ]:


def check(x):
    cnt = (6<=len(x) and len(x)<=12)
    for i in x:
        if i.isupper():
            cnt+=1
            break
    for i in x:
        if i.islower():
            cnt+=1
            break
    for i in x:
        if i.isnumeric():
            cnt+=1
            break
    for i in x:
        if i=='@' or i=='#'or i=='$':
            cnt+=1
            break
    return cnt == 5              

str = input().split(',')
list = filter(check,str)           
print(",".join(list)) 


# In[ ]:


import re
password = input()
re.search(r"([a-z]+[0-9]+[A-Z]+len(6,12))", password)


# In[ ]:


# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.


# In[ ]:


l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(',')))
print(l)


# In[ ]:


# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
# Hints:
# Consider use yield


# In[ ]:


def number(n):
    for i in range(0,n):
        if i%7 == 0:
            yield i
for num in number(100):
    print(num)


# In[ ]:


# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# In[ ]:


# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1


# In[ ]:


x = input().split()
word = sorted(set(x))     

for i in word:
    print("{0}:{1}".format(i,x.count(i)))


# In[ ]:


x = input().split()
dict = {i:x.count(i) for i in x}
dict = sorted(dict.items())

for i in dict:
    print("%s:%d"%(i[0],i[1]))


# In[ ]:


# Question:
#     Write a method which can calculate square value of number
# Hints:
#     Using the ** operator


# In[ ]:


n=int(input())
print(n**2)


# In[ ]:


# Question:
# Define a function which can compute the sum of two numbers.
# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.


# In[ ]:


sum = lambda n1,n2 : n1 + n2
print(sum(16,5))


# In[ ]:


# Question:
# Define a function that can convert a integer into a string and print it in console.
# Hints:
# Use str() to convert a number to string.


# In[ ]:


def print_val(n):
    print(str(n))
print_val(10)


# In[ ]:


conv = lambda x : str(x)
n = conv(10)
print(n)


# In[ ]:


# Question:
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
# Hints:
# Use int() to convert a string to integer.


# In[ ]:


sum = lambda x1,x2 : int(x1) + int(x2)
print(sum(10,25))


# In[ ]:


# Question:
# Define a function that can accept two strings as input and concatenate them and then print it in console.
# Hints:
# Use + to concatenate the strings


# In[ ]:


sum = lambda x1,x2 : x1 + x2
print(sum("10","25"))


# In[ ]:


# Question:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
# Hints:
# Use len() function to get the length of a string


# In[ ]:


def string_val(x1,x2):
    len1 = len(x1)
    len2 = len(x2)
    if len1>len2:
        print(x1)
    if len1<len2:
        print(x2)
    else:
        print(x1)
        print(x2)
print(string_val("one","two"))


# In[ ]:


# Question:
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
# Hints:
# Use % operator to check if a number is even or odd.


# In[ ]:


def number(n):
    if n % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
number(27)


# In[ ]:


# Question:
# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.


# In[ ]:


def printdict():
    dict={i:i**2 for i in range(1,3)}   # Using comprehension method and
    print(dict)

printdict()


# In[ ]:


# Question:
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.


# In[ ]:


def printdict():
    dict={i:i**2 for i in range(1,20)}
    print(dict)
printdict()


# In[ ]:


def printdict():
    dict={i:i**2 for i in range(1,20)}
    print(dict.keys())
printdict()


# In[ ]:


# Question:
# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.


# In[ ]:


def printlist():
    list=[i**2 for i in range(1,20)]
    print(list)
printlist()


# In[ ]:


# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list


# In[ ]:


def printlist():
    list = [i**2 for i in range(1,20)]
    for i in range(5):
        print(list[i])
printlist()


# In[ ]:


# Question:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list


# In[ ]:


def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(5,20):
        print(lst[i])

printList()


# In[ ]:


# Question:
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.


# In[ ]:


def printtuple():
    lst = [i**2 for i in range(1,21)]
    print(tuple(lst))
printtuple()


# In[ ]:


# Question:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
# Hints:
# Use [n1:n2] notation to get a slice from a tuple.


# In[ ]:


tup = (1,2,3,4,5,6,7,8,9,10)
tup2=tup[5:]
tup1=tup[:5]
print(tup1)
print(tup2)


# In[ ]:


tup = (1,2,3,4,5,6,7,8,9,10)
list1,list2 = [],[]
for i in range(0,5):
    list1.append(tup[i])
    
for i in range(5,10):
    list2.append(tup[i])
    
print(list1)
print(list2)


# In[ ]:


# Question:
# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
# Hints:
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.


# In[ ]:


tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(i for i in tpl if i%2 == 0)
print(tpl1)


# In[ ]:


tup = (1,2,3,4,5,6,7,8,9,10)
tup1 = {'evens': list(filter(lambda x: x%2 == 0, tup))}
tup1


# In[ ]:


# Question:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
# Hints:
# Use if statement to judge condition.


# In[ ]:


str = input()
if str.lower() == 'yes':
    print("Yes")
else:
    print("No")


# In[ ]:


# Question:
# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.


# In[ ]:


lst = [1,2,3,4,5,6,7,8,9,10]
lst1 = list(filter(lambda x: x%2 == 0,lst))
print(lst1)


# In[ ]:


lst = [1,2,3,4,5,6,7,8,9,10]
lst1 =[i for i in lst if i%2 ==0]
lst1


# In[ ]:


# Question:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.


# In[ ]:


lst = [1,2,3,4,5,6,7,8,9,10]
squaredno = map(lambda x: x**2, lst)
print(list(squaredno))


# In[ ]:


Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.


# In[ ]:


lst = [1,2,3,4,5,6,7,8,9,10]
squaredeven = map(lambda x: x**2, filter(lambda x: x%2==0, lst))
print(list(squaredeven))


# In[ ]:


# Question:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.


# In[ ]:


lst = filter(lambda x: x%2==0, range(1,21))
print(list(lst))


# In[ ]:


Question:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints:
Use map() to generate a list.
Use lambda to define anonymous functions.


# In[ ]:


lst =  map(lambda x: x**2, range(1,21))
print(list(lst))


# In[ ]:


# Question:
# Define a class named American which has a static method called printNationality.
# Hints:
# Use @staticmethod decorator to define class static method.


# In[ ]:


# Question:
# Define a class named American and its subclass NewYorker. 
# Hints:
# Use class Subclass(ParentClass) to define a subclass.


# In[ ]:


# Question:
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
# Hints:
# Use def methodName(self) to define a method.


# In[ ]:


class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius 
        self.area = radius * radius * Circle.pi
c = Circle(12)
print(c.area)


# In[ ]:


# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can 
compute the area. 
# Hints:
# Use def methodName(self) to define a method.


# In[ ]:


class Rectangle():
    def __init__(self,len,wid):
        self.len = len
        self.wid = wid
    def area(self):
        return self.len * self.wid
rect = Rectangle(22,45)
print(rect.area())


# In[ ]:


Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
Hints:
To override a method in super class, we can define a method with the same name in the super class.


# In[ ]:



    


# In[ ]:


Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:
Use try/except to catch exceptions.


# In[ ]:


try:
    x = 5/0
except:
    print("Error dividing by zero")
try:
    x = int("fred")
except:
    print("Error converting fred to a number")


# In[ ]:


# Define a custom exception class which takes a string message as attribute.
# Hints:To define a custom exception, we need to define a class inherited from Exception.


# In[ ]:


# Question:

# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Hints:
# Use \w to match letters.


# In[ ]:


import re
emailaddress = input()
pattern = "(\w+)@(\w+)\.(com)"
reg = re.match(pattern,emailaddress)
print(reg.group(1))


# In[ ]:


# Question:

# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# google
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Hints:
# Use \w to match letters.


# In[ ]:


import re
emailaddress = input()
pattern = "(\w+)@(\w+)\.(com)"
reg = re.match(pattern,emailaddress)
print(reg.group(1))


# In[ ]:


# Question:

# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
# Example:
# If the following words is given as input to the program:
# 2 cats and 3 dogs.
# Then, the output of the program should be:
# ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Hints:
# Use re.findall() to find all substring using regex.


# In[ ]:


import re
str = input()
print(re.findall("\d+",str))


# In[ ]:


Question:

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints:
Use float() to convert an integer to a float.


# In[ ]:


n=int(input("Enter the number of terms: "))
val=0
for i in range(1,n+1):
    val = val + float(float(i)/(i+1))
print(round(val,2))


# In[ ]:


# Question:

# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
# with a given n input by console (n>0).
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 500
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Hints:
# We can define recursive function in Python.


# In[ ]:


def num(n):
    if n == 0:
        return 0
    else:
        return num(n-1)+100
print(num)

n = input()
print(num(5))


# In[ ]:


x = int(input(lambda x:0 if (x==0) else ((x-1)+100), x)


# In[ ]:


# Question:

# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program to compute the value of f(n) with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 13
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Hints:
# We can define recursive function in Python.


# In[2]:


def num(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: return (n-1)+(n-2)

x=int(input())
print(num(x))


# In[11]:


# Question:
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
# Example:
# If the following n is given as input to the program:
# 7
# Then, the output of the program should be:
# 0,1,1,2,3,5,8,13
# Hints:
# We can define recursive function in Python.
# Use list comprehension to generate a list from an existing list.
# Use string.join() to join a list of strings.
# In case of input data being supplied to the question, it should be assumed to be a console input.


# In[32]:


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1)+f(n-2)

n=int(input())
output = [str(f(x)) for x in range(0, n+1)]
print(",".join(output))

