#!/usr/bin/env python
# coding: utf-8

# # FUNCTIONS AND OUTCOMES

# > **Best way of programming is done by dividing a big program into smaller modules and repeatedly call these modules.**
# 
# > **Can be achieved by using functions**
# 
# > **Code's Readability and flow of execution of small modules can be managed easily**

# In[31]:


# Syntax and Basics of a Function


# In[32]:


def function_name(Parameters):  # -----------------> Function Header
############# Function Body #############
    statement1 
    statement2
    statement3
    #---------
    #---------
    statementN


# #### ***def*** - Keyword which signifies the beginning of the function's definition. Name of Function is followed by function's definition
# #### ***Function Header*** -  may contain zero or more number of parmeters. These are called Formal Parameters.
# #### ***Function's Body*** -  is block of statements which defines the actions.

# # Function Junction

# In[12]:


def display():
    """Prints 'Hello World!' to the console."""
    print("Hello World!")


# # Call and Response

# **After defining a function, it must be called to be implemented.**

# In[34]:


display()


# #### Write program to add the sum of numbers starting from 1 to 25, 50 to 75 and 90 to 100 using three different for loops

# In[1]:


sum = 0
for i in range(1,26):
    sum = sum+i
print("Sum of integers from 1 to 25 is = ", sum)

sum = 0
for i in range(50,76):
    sum = sum + i
print("Sum of integers from 50 to 75 is = ", sum)

sum = 0
for i in range(90, 101):
    sum = sum + i
print("Sum of integers from 90 to 100 is = ", sum)


# #### Simplifying the above program using Functions

# In[4]:


def sum(x,y):
    sum = 0
    for i in range(x,y+1):
        sum = sum + i
    print('Sum of integers from {} to {} is {}'.format(x,y,sum))


# In[3]:


sum(1,25)
sum(50,75)
sum(90,100)
sum(10,45)


# In[11]:


def square(n):
    squared = n ** 2 


# - %d is used as a place holder for numeric or decimal values.
# - %s is used for strings

# In[9]:


square(6)


# # Parameters and Arguments

# In[1]:


def power(base, exponent):  # Add your parameters here!
    result = base ** exponent
    print ("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)  # Add your arguments here!


# - %d is used as a placeholder for numeric or decimal values
# - The %d is for numbers, and %s is for strings.

# ### argument
# - A value passed to a function (or method) when calling the function. There are two types of arguments:
# 
# keyword argument: 
#     an argument preceded by an identifier (e.g. name=) in a function call or passed as a value in a dictionary preceded by **.
# - For example, 3 and 5 are both keyword arguments in the following calls to complex():

# In[3]:


complex(real=3,imag=5)


# In[5]:


complex(5,3)


# In[7]:


complex(**{'real': 3,'imag': 5})


# ### Positional argument: 
# 
# an argument that is not a keyword argument. Positional arguments can appear at the beginning of an argument list and/or be passed as elements of an iterable preceded by *. For example, 3 and 5 are both positional arguments in the following calls:
# 

# In[9]:


complex(3, 5)


# In[10]:


complex(*(3, 5))


# In[11]:


def Positional_Arguments(place, pincode):
    print("Place = {} and Pincode = {}".format(place, pincode))
Positional_Arguments("Hyderabad", 500082)
Positional_Arguments(500019,"Nizampet")
Positional_Arguments(pincode="500068",place = "LBNGAR") # Keyword arguments


# # Keyword Arguments

# In[11]:


def show(name,age):
    print("Name = {}, Age = {}".format(name,age))
    
show(age = 70, name = 'Rajinikanth')


# # Parameters with Default Arguments

# In[23]:


def area_circle(r,pi=3.14):
    Area = pi*r**2
    print("Area of Circle is multiplying the square of radius {} with pi {} and the result {} ".format(r,pi,Area))


# In[22]:


area_circle(5)


# # Overriding the Default Arguments is possible ?
# 
# ***Yes, it's possible***

# In[5]:


area_circle(5,10)


# # Local and Global Scope of a Variables
# 
# - ***Variables and parameters that are initialized within a function including parameters, are said to be exist in that function's local scope. Variables that exist in local scope are local variables***
# - ***Variables that are assigned outside function are said to exist in global scope. Therefore, variables that exist in global scope are called global variables***

# In[2]:


p = 20
def global_local_example():
    q = 10
    print("Local Variable value",q)
    print("Global Variable value",p)
print("Global Variable value accessing outside function",p)
#print("Local Variable value",q)
global_local_example()


# In[7]:


p = 20
def globals_locals_examples():
    q = 10
    print("Local Variable value",q)
    print("Global Variable value",p)
print("Global Variable value accessing outside function",p)
#print("Local Variable value",q)
globals_locals_examples()


# # Local and Global Variables with same name

# In[2]:


a = 20
def same():
    a = 10
    print(a)
same()
print(a)


# In[3]:


def aravind(x):
    return x


# In[4]:


aravind(20)


# # Global Statement

# - If a variable is assigned a value anywhere with in the function's body,it's assumed to be a local unless explicitly declared as global

# In[6]:


a = 20
def global_statement():
    global a
    print("Global :",a)
    a = 30
    #print("Value of a inside function = ", a)
global_statement()
print("Value of a outside function = ", a)


# # Functions Calling Functions
# ## Return Statement

# In[7]:


def first_function(n):
    return n + 1
    
def second_function(n):
    return n + 2 # return statement is used to return a value from the function / break out of a function.


# In[9]:


second_function(10)


# In[10]:


def first_function(n):
    return n + 1
    
def second_function(n):
    return first_function(n) + 2


# In[11]:


second_function(10)


# In[12]:


a = 20
def global_statement(x):
    global a
    print("Global :",a)
    return x
    
global_statement(2)


# #### without Global

# In[26]:


a = 20
def without_global_statement(a):
    print("without global :",a)
    return a    
without_global_statement(2)


# In[101]:


def area_rect(l,b):
    if l<0 or b<0:
        return # if function does not return anything, the default value function return is none
    else:
        print("Length = {}, Breadth = {}".format(l,b))
        return l*b
    
    
area_rect(-1,6)


# # Return Multiple Values to variable(s)

# In[13]:


def square_cube(num):
    print("Number = ", num)
    return num*num, num*num*num


square,cube = square_cube(4)
print("Square = ", square, "Cube = ", cube)


# # Write a program to find cube of a number and check if the cube is divisible by 3 or not (Hint : use one function in function)

# In[19]:


def cube(number):
    return number**3
def by_three(number):
    if number%3 == 0:
        result = cube(number)
        return result
    else:
        return False


# In[20]:


by_three(9)


# # Built in Functions

# # One Example of how to use a built in Function

# ### ( *args)  used to write anythings in it as a input 

# In[29]:


def biggest_number(*args):
  print(max(args))
  return max(args)
    
def smallest_number(*args):
  print(min(args))
  return min(args)

def distance_from_zero(arg):
  print(abs(arg))
  return abs(arg)


# In[30]:


biggest_number(-10, 20.5)


# In[17]:


biggest_number(-10, -5, 5, 10)


# In[18]:


smallest_number(-10, -5, 5, 10)


# In[21]:


distance_from_zero(-10)


# In[38]:


def dd(*args):
    return str(args)


# In[44]:


dd("python")


# In[26]:


print(type(45))
print(type(4.5))
print(type("Hello"))


# # Write a program to find a square root of a number

# In[16]:


def factors():
    num = int(input("Enter a number to find multiples of number :"))
    for i in range(1,num+1):
        if num%i == 0:
            print(i)
        
    for i in range(1,num+1):
        if i*i == num:
            print("Square root of {} is {}".format(num,i))
multiples()


# ## Write factors of a numbers

# In[20]:


def factors():
    
    num = int(input("Enter a number to find factors of number :"))
    for i in range(1,num+1):
        if num%i == 0:
            print(i)


# In[21]:


factors()


# In[113]:


import math 
# from math import *
# from math import sqrt


# In[114]:


print(math.sqrt(64))


# In[115]:


import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!


# In[33]:


def shut_down(s):
  if s == "yes":
    return "Shutting Down"
  elif s == "no":
    return "Shutdown Aborted"
  else:
    return "Sorry"
shut_down("yes")


# In[ ]:


# Write a program to create a function and print the absolute value of number if the type of number is int or float.


# In[34]:


def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"


# In[35]:


distance_from_zero(-15.6)


# # Tasks
# 
# - Calculate distance between two points sqrt((x2-x1)^2 + (y2-y1)^2)
# - For a Quadratic Equation ax^2 + bx + c the discriminant D is (b^2 - 4ac). Write a function to compute the discriminant D, that returns the following output depending on the discriminant D.
#   
#   ***Conditions:***
#       - if D>0: The Equation has two Real roots
#       - if D=0: The Equation has one Real root
#       - if D<0: The Equation has two Complex roots.

# # Changing the functionality of a function

# ### Change the function so the given argument is multiplied by 3 and returned.

# In[1]:


number = 5

def my_function(x):
  return x * 3

print(my_function(number))


# # More than one argument

# ### Shows how to use more than one argument in a function.

# In[3]:


m = 5
n = 13
# Add add_function here!
def add_function(x,y):
  return x+y


print(add_function(m, n))


# # Strings in functions

# In[2]:


n = "Hello"
# Your function here!
def string_function(s):
  return s+' world'


print(string_function(n))


# # Passing a list to a function

# ### Can pass a list to a function the same way you pass any other argument to a function.

# In[22]:


def list_function(x):
  return x

n = [3, 5, 7]
print(list_function(n))


# In[23]:


def list_function(x):
  return x[1]

n = [3, 5, 7]
print(list_function(n))


# # Modifying an element of a list in a function

# In[24]:


def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print(list_function(n))


# # List manipulation in functions

# ### You can also append or delete items of a list inside a function just as if you were manipulating the list outside a function.

# In[30]:


n = [3, 5, 7]
# Add your function here
def list_extender(lst):
  lst.append(9)
  return lst


print(list_extender(n))


# # Printing out a list item by item in a function

# ### The below code shows how to utilize every element in a list in a function.

# In[31]:


n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print(x[i])
    
print_list(n)


# # Modifying each element in a list in a function

# ### The below code shows how to modify each element in a list.

# In[15]:


n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
# Don't forget to return your new list!

print(double_list(n))


# # Passing a range into a function

# ### The Python range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.

# In[19]:


a = []
def my_function(x):
  for i in range(0, len(x)):
    a.append(i)
  return a

print(my_function(range(3))) # Add your range between the parentheses!


# # Iterating over a list in a function

# In[20]:


n = [3, 5, 7]

def total(numbers):
  result = 0
  for item in numbers:
    result = result + item
  return result
  
print(total(n))


# # Using strings in lists in functions

# In[22]:


n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ''
  for item in words:
    result = result + item
  return result


print(join_strings(n))


# # Using two lists as two arguments in a function

# ### Using multiple lists in a function is no different from just using multiple arguments in a function!

# In[32]:


m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
  return x + y


print(join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]


# # Using a list of lists in a function

# ### The below code shows how to make use of a single list that contains multiple lists and how to use them in a function.

# In[25]:


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def combine(lists):
  results = []
  for list1 in lists:
    for number in list1:
      results.append(number)
  return results

print(combine(n))


# In[16]:


lists = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
results= []
for i in lists:
    for j in i:
        results.append(j)


# In[17]:


results


# In[ ]:




