#!/usr/bin/env python
# coding: utf-8

# 1.1 Install Jupyter notebook and run the first program and share the screenshot of the output.

# <img src="files/ss.png" width="600" height="300">

# 2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple
#    of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
#    comma-separated sequence on a single line.

# In[28]:


l=[]
for i in range(2000,3201):
    num=i
    if num%7==0 and num%5!=0:
        l.append(i)
print(l)


# 3. Write a Python program to accept the user's first and last name and then getting them printed in
#    the the reverse order with a space between first name and last name.

# In[29]:


l=[]
print("Enter the name")
l.append(input())
print("Enter the last name")
l.append(input())
print(*l[::-1],sep=' ')


# 4.  Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3

# In[30]:


r=12
print("volume of a sphere =",((4/3)*(22/7))*r*r*r)


# 5. Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.

# In[31]:


print("Enter th number")
a=input()
b=a.split(',')
b


# 6.  Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# In[32]:


for i in range(5):
    for j in range(i+1):
        print("* ",end='')
    print("\n")
for i in range(4):
    for j in range(4-i):
        print("* ",end='')
    print("\n")


# 7. Write a Python program to reverse a word after accepting the input from the user.
# Sample Output:
# Input word: AcadGild
# Output: dilGdacA

# In[33]:


print("Enter the word")
a=input()
a[::-1]


# 8. Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens

# In[34]:


print('WE, THE PEOPLE OF INDIA')
print("\thaving solemnly resolved to constitute India into a SOVEREIGN, !")
print("\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC")
print("\t\t  and to secure to all its citizensNOTE")

