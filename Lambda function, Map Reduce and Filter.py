#!/usr/bin/env python
# coding: utf-8

# ### Lambda function in python
# - A lambda function is a small anonymous function.
# 
# - A lambda function can take any number of arguments, but can only have one expression.
# 
# #### Syntax
# 
# lambda arguments : expression
# 
# The expression is executed and the result is returned:

# In[2]:


def addition(a,b):
    c = a+b
    return c


# In[3]:


addition(1,2)


# ***more simpler way***

# In[4]:


def addition1(a,b):
    return a+b


# In[5]:


addition1(1,2)


# ***more simpler way***

# In[7]:


def addition2(a,b): return a+b


# In[8]:


addition2(2,3)


# ***more simpler way***

# In[4]:


add_lam = lambda a,b: a+b


# In[11]:


add_lam(5,3)


# **Create a lambda function to find even numbers**

# In[18]:


find_even = lambda x : x%2 == 0


# In[10]:


find_even(13)


# **Similarly find odd**

# In[19]:


find_odd = lambda x : x%2 != 0


# In[6]:


find_odd(18)


# Lambda functions can take any number of arguments:
# 
# ##### Why Use Lambda Functions?
# - The power of lambda is better shown when you use them as an anonymous function inside another function.
# - Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
# - An anonymous function is a function with out a name
# - While normal functions are defined using the def keyword in python ,anonymous functions are defined using lambda keyword.
# - We use lambda functions when we require a nameless function for a short period of time.
# - Lambda functions are used aong with built-in functions like filter(),map()

# In[8]:


def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mydoubler(12)


# - Use that function definition to make a function that always doubles the number you send in:

# In[9]:


def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
my4times  = myfunc(4)

print(mydoubler(11))
print(mytripler(11))
print(my4times(11))


# - Or, use the same function definition to make a function that always triples the number you send in:

# In[3]:


def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


# - Or, use the same function definition to make both functions, in the same program:

# In[10]:


def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


# - Use lambda functions when an anonymous function is required for a short period of time.
# 

# ### Create a list from 300 to 700 with a step of 3 
# 
# - in that list1 find even numbers and prepare new list and name it as list2
# 

# In[15]:


List1 = list(range(300,700,3))
type(List1)


# In[16]:


print(List1)


# ### Without lambda function using for and if looping to identify the even numbers from list1

# In[17]:


List2 = [] # Creating an empty list
for i in List1:
    if i%2 == 0:
        List2.append(i) # Appending the even numbers to the empty list
print(List2)


# ### lambda function

# In[20]:


List2 = []
for i in List1:
    if find_even(i):
        List2.append(i)
print(List2)


# ***more simpler way***
# 
# # Filter
# 
# **Takes a function and list as arguments**

# In[17]:


list2 = list(filter(find_even,list1))


# In[22]:


print(list2)


# ### find out the values in list1 which are divided by 5 using filter

# In[20]:


def find_div_5(num):
    return num%5 == 0


# In[21]:


find_div_5_lam = lambda num : num%5 == 0


# In[22]:


list3 = list(filter(find_div_5,List1))
list4 = list(filter(find_div_5_lam,List1))


# In[23]:


print(list3)


# In[24]:


print(list4)


# **find a list with values in list1 which are not divisible by 5**

# In[19]:


list4 = filter(lambda num : num%5 != 0, List1)
print(list4)


# In[20]:


print(list(list4))


# In[7]:


print(list1)


# In[2]:


# Method 1 without map
List1 = list(range(300,700,3))
list5 = []
for i in List1:
    list5.append(i-300)
    
print (list5)


# # Map
# 
# **map(func,iterables)**
# 
# - Making an iterable computes the function using arguments with each iterables
# 
# ### In list1 subtract all values with 300

# In[23]:


# Method 2 to subtract all values
sub_lam = lambda x : x - 300


# In[25]:


list6 = map(sub_lam,List1)
print(list(list6))


# ### find square of all values in list1

# In[26]:


pow = lambda x : x**2


# In[28]:


list7 = map(pow,List1)


# In[29]:


print(list(list7))


# ### Sum of elements in the list1

# In[4]:


num = 0
for i in List1:
    num = num + i    
print(num)


# # Reduce
# 
# **Takes two arguments cummulatively and reduces the sequence**

# In[13]:


addition = lambda x,y : x+y


# In[14]:


print(List1)


# In[11]:


import functools 
from functools import reduce


# In[12]:


reduce(addition,List1)


# In[19]:


list10 = [50,55,60,65,70,72,99,54,10,201,210,98,300,110,123]


# In[18]:


find_greater = lambda x,y : x if x>y else y
find_greater(30,45)


# In[20]:


list11 = [50,110,100,95]
reduce(find_greater,list11)


# In[21]:


reduce(find_greater,list10)


# **Difference between Map and Filter**

# In[45]:


print(list1)


# In[37]:


list4 = filter(lambda num : num%5 != 0, List1)
print(list(list4))


# In[38]:


list4 = map(lambda num : num%5 != 0, List1)
print(list(list4))


# In[ ]:





# In[ ]:




