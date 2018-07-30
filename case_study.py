
# coding: utf-8

# In[15]:


get_ipython().run_line_magic('reset', '-f')
#https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt


# In[16]:


# Q-1 Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).


# In[17]:


# 1 
for i in range(2000,3200):
    if i % 7 == 0 and i % 5!=0:
        print(i)


# In[18]:


# 2         
num = list(range(2000,3200))
num = filter(lambda x : x % 7 == 0 and  x % 5 != 0, num)
num = list(num)
print(num)


# In[19]:


#3
print(list(filter(lambda x: x%7 == 0 and x%5 !=0, list(range(2000,3200)))))        


# In[20]:


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


# In[21]:


numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
          ]

numbers1 = [i for i in numbers if i%2 == 0 and i <= 237] 
numbers1


# In[24]:


# Q-3   Write a program which can compute the factorial of a given numbers.
#    The results should be printed in a comma-separated sequence on a single line.
#    Suppose the following input is supplied to the program:
#    8
#    Then, the output should be:
#    40320


# In[25]:


fact = lambda x : 1 if x == 0 else x * fact(x-1)
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


# In[30]:


row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)


# In[42]:


# Q-5
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number
# between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program:
#8 Then, the output should be:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


# In[43]:


d = dict()
for i in range(1,i):
    d[i] = i**2
print(d)


# In[46]:


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


# In[77]:


import numpy as np
values = input("comma separated numbers : ")
l = values.split(",")
print('list :', l)


# In[80]:


t = tuple(l)
print(t)

