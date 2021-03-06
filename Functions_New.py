#!/usr/bin/env python
# coding: utf-8

# # FUNCTIONS

# > **A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.**
# 
# > **Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.**
# 

# ### Syntax of Function

# In[1]:


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

# In[1]:


#This prints a passed string into this function

def printstr(str):
    print(str)

#Calling a function
printstr("Welcome to Codeworld")
printstr("This is July batch")


# In[3]:


def name(name):
    print(name + " " + "Roy")

#Calling a function
name('Danish')
# Calling a function using a variable
n = "Ram" 
name(n)  


# In[5]:


#Function with two arguments
def name(name,surname):
    print("His name is "+ name + " " + surname)

name('Danish','Kapoor')


# In[6]:


name("Aravind")


# In[10]:


def add(x, y):
    result = x + y
    print(x, "+", y ,"is", result)
    
x = 6
y = 8
add(x, y)


#or you can directly give value of arguments
add(10,3)


# In[3]:


# Default Arguments
def sub(a = 8 , b = 5):
    diff = a - b
    print(a, "-", b ,"is", diff)
    
sub() 

#when given values of arguments
sub(5,7)


# In[6]:


def sub(a , b = 5): # Default Arguments
    diff = a - b
    print("%d subtracted from %d  is %d" % (b , a , diff))
    
sub(100,10)


# In[7]:


#Python function to check whether x is even or odd 
def checknum( x ): 
    if (x % 2 == 0): 
        print("even")
    else: 
        print("odd")
        
checknum(7) 
checknum(22) 


# In[20]:


# Return Multiple Values to variable(s)
def square_cube(num):
    print("Number = ", num)
    return num*num, num*num*num
se
square,cube = square_cube(4)
print("Square = ", square, "Cube = ", cube)


# In[22]:


def change(x): 
    x[0] = 20

Lst = [10, 11, 12, 13, 14, 15]  
print('Before:',Lst) 
print('After:',Lst)


# In[27]:


#This function returns the absolute value of the entered number
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(5))

print(absolute_value(-1.5))


# In[31]:


#Passing a List as an Argument
def fruits_name(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

fruits_name(fruits)


# # List manipulation in functions
# ### You can also append or delete items of a list inside a function just as if you were manipulating the list outside a function.

# In[33]:


n = [3, 5, 7]

def list_extender(lst):
    lst.append(9)
    return lst


list_extender(n)


# In[41]:


m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
    return x + y


print(join_lists(m, n))


# In[ ]:




