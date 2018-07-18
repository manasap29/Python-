#%reset -f
#%%
#Methods in python(append)
my_list = [1,2,3]
my_list.append(4)
my_list
#pop
my_list = [1, 2, 3, 4]
my_list.pop()
my_list
#how to get methods in python(in jupyter shift+tab)
#here i gave an index and then value to insert into the list
mylist = [1,2,3]
mylist.insert(3,4)
print(mylist)
#%%
#091 Functions in Python(Includes general concepts and questions)
#Return allows to assign the output to the new variable
#Creation
def my_function():
    print("Hello") 
#created a new function,how to call the function?
my_function()
#Here i gave 'Name' as an input,so during calling the func. i have to give name.
def my_function(name):
    print("Hello" + name)
my_function('Aryan')
#i can give a default name
def my_function(name = 'NAME'):
    print("Hello" + name)
my_function('Aryan')
#Write a function and return the value of variable of the function
def my_func ():
    x = 10
    print("value inside the function :", x)
y = 20
my_func()
print("value is outside the function :", y)    
#how to pass default value to the function
def my_func(country = "India"):
    print("I am from " + country)
my_func("India")
#
def func_one(vegetables = "potato"):
    print("i am fond of" + vegetables)
func_one( "Carrot")
#how to write a function that Returns Values
def add(n1,n2):
    return(n1 + n2) 
result = add(20,30)
print(result)
#Check the case here the price returns the output as 'True'
def price_check(mystring):
    if 'price' in mystring:
        return True
    else:
        return False
price_check('price of the toy is Rs 50')    
#Let's check another case where error is due to "P" upper case.It shows "False"
def price_check(mystring):
    if 'price' in mystring:
        return True
    else:
        return False
price_check('Price of the toy is Rs 50') 
#Then i have to change the function as follows
def price_check(mystring):
    if 'price' in mystring.lower():
        return True
    else:
        return False
#The above function doesn't need "if" statement as it is already"Boolean"
#we can write it more precisely,where no if,else is required
def price_check(mystring):
    return'price' in mystring.lower()
price_check('Price of the toy is Rs 50') 
#Another example
def my_func(x):
    return 5 * x
print(my_func(3))
#Another Example see how it works
def pig_latin(word):
    first_letter = word[0]
#we will check the vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
#here you check the status for both the words.
pig_latin('carrier')
pig_latin('apple')    
# Write a function that returns the absolute number
def absolute_number(num):
    if num >= 0:
        return num
    else:
        return -num
print(absolute_number(4))
print(absolute_number(-4))
#Write a function that gives the average of two numbers.
#always the return need to be outside the function.
def avg_num(x,y):
    print("Average of ",x, "and", y,"is ",(x+y)/2)
avg_num(3,4)
#Write a function that returns the multple of three numbers
def multiple_value(x,y,z):
    print("The expected value of", x,y,z,"is", x*y*z)
multiple_value(7,8,9)
#Write a function that returns the square of sum of two values.
def square_sum(x,y):
    return(x*x+2*x*y+y*y)
    print("The square of sum of 2 and 3 is :", square_sum(2,3))
square_sum(8,9)
#
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;
printme("Outside is cloudy")
#
def changeme(mylist):
    "This change is passed to the function"
    mylist.append([1,2,3,4,5,6])
    print("Values inside the function: ", mylist)
    return
#%%
#044 args(arguments) and kwargs(keyword arguments) 
# check the follwing function
def myfunc(a,b):
# here a nd b are positional arguments
#we need to return 5% of a+b
  return sum((a,b))*0.05
myfunc(50,60)
# when the numbers are more,we need to pass more parameter
#new func where "args" is used,arbitrary no of arguments
#It returns tuples of values
def myfunc(*args):
    return sum(args)*0.05
myfunc(50,60,120,210,600,230)
#here instead of "args"(abcd) we can write anything, actually * is working
def myfunc(*abcd):
    return sum(abcd)*0.05
myfunc(50,60,120,210,600,230)
#Another modification to the above example
def myfunc(*abcd):
    for item in abcd:
        print(item)
myfunc(50,60,120,210,600,230)
#The same logic is applicable to "Key word arguments",hence we use "kwarg"
#It results a dictionary for "kwarg"
def myfunc(**kwarg):
    if 'fruit' in kwarg:
        print('I would like to have {}'.format(kwarg['fruit']))
    else:
        print('I did not have a fruit here')
myfunc(fruit = 'apple')
#By convention (**) only working,we can take anything insted of "kwarg" 
#Demonstrate an example which uses both "args" & "kwargs"
def myfunc(*args,**kwargs):
    print("I would like {} {}".format(args[0],kwargs['food']))
myfunc(10,20,30,fruit = 'orange',food = 'egg',animal = 'elephant' )
#we need to check always check the order of the "arguments"
#%%
#lambda functions 

#%%
# Map and Filter
def square(num):
    return num**2
my_nums = [1,2,3,4,5]
#if we want to square list of numbers,we can use a for loop,but we can do it 
#with "map function" asily.
for item in map(square,my_nums):
    print(item)
#if i wan't to see my list back, i will write
list(map(square,my_nums))
#Another example for refernce.We are passing "function" as an argument to "Map"
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
names = ['Arab','Aryan','Arpita']
list(map(splicer,names))
# Filter function
#we are passing a function into filter is either "True" or "False"
def check_even(num):
    return num%2 ==0
mynums = [1,2,3,4,5,6,7]    
#now filter will do the job for finding even & odd in the list.
list(filter(check_even,mynums))
#%%
# Lambda expresion is an annonymous function
def square(num):
    result = num**2
    return result
# Now we are changin to a lambda expresion
square = lambda num: num**2
square(5)
#we can use in conjunction with "Map" and "Filter"
list(map(lambda num:num**2,mynums))
#let's use with "Filter" function
list(filter(lambda num:num%2 == 0,mynums))
# it returns only even number.
# See a case where we are using Lambda expresion
names = ['Arab','Aryan','Arpita']
list(map(lambda name:name[0],names))
#It will display the first letter of list.
#%%
#create a function that gives square,cubes etc of integers
myfunc = lambda i : i**2
print(myfunc(3))
#
myfunc = lambda i : i**4
print(myfunc(5))
#
myfunc = lambda i : i**3
print(myfunc(6))
#
myfunc = lambda i: i**5
print(myfunc(2))
#create a function that multiplies two integers
myfunc = lambda x,y : x*y
print(myfunc(5,6))
#create a function which creates an anonymous function #that multiplies 
#variable i with variable n.
def myfunc(n):
    return lambda i : i*n
double = myfunc(2)
triple = myfunc(3)
val = 11
print ("Double: " + str(double(val)) + "Triple: " + str(triple(val)))
#%% Test cases
#Out of two even numbers show the smaller one but return the greater if one or both 
#of them are odd.
def lesser_even(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
lesser_even(2,4)
lesser_even(6,7)
#Write a Python function to find the Max of two,three numbers.
def max_two(x,y):
        if x > y:
            result = x
        else:
            result = y
        return result
max_two(2,3)
#defining max out of three numbers
def max_three(x,y,z):
    return max_two(x,max_two(y,z))
max_three(2,6,-1)
#Write a function to sum all the numbers in the list
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((1,3,8,42,-12)))
#Write a function to multiply all the numbers in the list
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total  
print(multiply((12, 4, 2, 9, 6, -2)))        
#write a function takes a two word string and returns true if both
#word begins with the same letter.
def check_string(text):
    wordlist = text.split()
    print(wordlist)
    one = wordlist[0]
    two = wordlist[1]
    return one[0] == two[0]
check_string("baby boy")
check_string("baby girl")        
#another smart way of doing it is 
def check_string(text):
    wordlist = text.lower().split()
    print(wordlist)
    return wordlist[0][0] == wordlist[0][1]       
check_string("python console")        
#Write a function that returns a reversed string.
def reverse_string(str1):
    return str1[::-1]
reverse_string('collaboration')
#Python function to calculate the factorial of a number (a non-negative integer).
#The function accepts the number as an argument.    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
#Write a Python function to check whether a number is in a given range.
def test_range(n):
    if n in range(3,9):
        print("%s is in the range" %str(n))
    else:
        print("The number is outside the range")
test_range(11)   
#
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print(unique_list([1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,5])) 
#white a function that gives an input number is a prime number or not.
number = int(input("Enter any number :"))
if number > 1:
    for i in range(2,number):
        
        if(number % i) == 0:
            print()
        print(number,"is not a prime number")
        break
    else:
        print("It is not a prime number")
#Write a Python function that checks whether a passed string is palindrome or not.
#A palindrome is a word, phrase, or sequence that reads the same backward 
#as forward, e.g., madam or nurses run.
def ispalindrome(string):
    left = 0
    right = len(string) -1
    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1
        right+= 1
    return True
print(ispalindrome('adam'))
#Writing a function that focuses on first and fourth letter of 
# a word and amkes it upper case.
def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize()+ second_half.capitalize()
old_macdonald('macdonald')           
#Reverse a string
def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    return reverse_word_list
master_yoda('i am at home')  
# Write a function that 'joins' the lists together.
mylist = ['a','b','c']
''.join(mylist)
#almost there(absolute function) in python
complex = (3 - 4j)
print('Absolute value/Magnitude of complex is:', abs(complex))
#
float = -54.36
print('Absolute value/Magnitude of float is: ',abs(float))
#
int = -94
print('Absolute value/Magnitude of float is: ', abs(int))
#The function checks where there is a same letter repeated after that,
#if so returns True or return False.  
def has_33(nums):
    for i in range(0, len(nums)-1): 
        if nums[i:i+2] == [3,3]:
            return True  
    return False
has_33([2, 2, 3])
has_33([2, 3, 3])
#
def numbers(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <= 31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
numbers(5,9,17) 
numbers(6,1,3)
#%%       
# Nested Statements    
# LEGB RULE = Local -> Enclosed -> Global -> Built-in.
# This is the order in which python used look for the variables in python.
# Local namespace = def,lambda     
# Enclosed= names in local scope of any and all enclosed funcion(def or lambda),
# from inner to outer.
# Global(Module) = name asiigned at top/declared global in a def   
# Built-in(Python).= names preassigned in the built name(open,range)
#Examples of LEGB function:
# i is local.
f = lambda i:i**2       
#Enclosed function example
name = 'This is a global name'
def wish():
# Enclosing function
    name = 'Aryan'
    def hello():
        print('Hello '+ name)
    hello()
wish()
#Global(Module)
print(name) 
# Built in function example
len()       
x = 50
# Local variable example,a function outside the defined func.
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is still', x)        
# write a function measuring the volume of sphere:
def vol(rad):
    return(4/3)*(3.141)*(rad**3)
vol(7)
#Write a function that checks whether a number is in a given range
#(inclusive of high and low)
def num_check(num,low,high):
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('It is outside the range.')
num_check(2,6,12)
num_check(3,1,9)
# Another method
# we can also write a func using bollean to chek.Only Bollean as output
def num_bool(num,low,high):
    return num in range(low,high+1)
num_bool(5,3,9)
num_bool(11,11,15)
#
    
        
        
        
        
            
        
        
        
        
        
        
        
              










