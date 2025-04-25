#!/usr/bin/env python
# coding: utf-8

# In[13]:


"""
4.	Напишіть функцію, яка приймає ціле число та повертає суму всіх його цифр. Наприклад, 437. 4+3+7=14.
"""

def sum_num():
    numb = str(input("Enter the number "))
    lens = len(numb)
    summery = []
    for x in range(lens):
        summery.append(int(numb[x]))
    return sum(summery)
        
testing = sum_num()
print(testing)


# In[ ]:




