#!/usr/bin/env python
# coding: utf-8

# In[9]:


"""
2.	Напишіть функцію, яка приймає довільну кількість словників, збирає їх в один словник та повертає його.
"""

my_list = []

def dicts(**kwargs):
    my_list.append(kwargs)
    for i in my_list:
        return i

testing = dicts(a=1, b=2, c=3)
print(testing)


# In[ ]:




