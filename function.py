c:\any\dir> spyder --reset
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
def name_func():
    '''
    DOCSTRING: Information about the function
    '''
    INPUT:no input
    OUTPUT: Hello   
    print(Hello)
#
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
#%%














