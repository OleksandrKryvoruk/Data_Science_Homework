#!/usr/bin/env python
# coding: utf-8

# In[22]:


"""
5.	Напишіть функцію, яка приймає рядок та повертає літеру, яка зустрічається в ньому найчастіше.
"""
from collections import Counter

def count(s):
    s = s.replace(' ','')
    lst = list(s)
    res_dict = Counter(lst)
    result = res_dict.most_common(1)
    return result
        
testing = count("Напишіть функцію, яка приймає рядок та повертає літеру, яка зустрічається в ньому найчастіше")
print(testing)


# In[ ]:




