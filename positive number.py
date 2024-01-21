#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python program to print all positive numbers in a range.

# Get input from the user
list1 = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
positive_numbers = [num for num in list1 if num > 0]

# Get positive numbers
positive_numbers = get_positive_numbers(list1)

# Print the result
print("Output:", positive_numbers)

