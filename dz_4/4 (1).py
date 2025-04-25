#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""
1.	Напишіть функцію, яка приймає номер місяця та повертає рядок з назвою пори року, 
до якої цей місяць відноситься.
"""

my_times = {1:'winter', 2:'winter', 3:'spring', 4:'spring', 5:'spring', 6:'summer',
            7:'summer', 8:'summer', 9:'autumn', 10:'autumn', 11:'autumn', 12:'winter'}


def times():
    choice = int(input('Enter the number of mounth (1-12) - '))
    return my_times[choice]

testing = times()
print(testing)


# In[ ]:




