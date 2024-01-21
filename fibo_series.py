#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#python program for fibonacci series
n= int(input("Enter the number of terms: "))
a =0 #first number
b =1 #second number

if n<=0:
    print(a)
else:
    print(a)
    print(b)
    for x in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c

