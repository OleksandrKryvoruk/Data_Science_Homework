#!/usr/bin/env python
# coding: utf-8

# In[147]:


"""
3.	Створіть функцію, яка приймає рядок з назвою файлу, створеного функцією з попереднього завдання. Функція має зчитувати 
файл, записувати кожну пару ключзначення у словник та повертати цей словник.
"""

def file(*args):
    
    with open(f'{args}.txt', "r") as fq:
        print(fq.read())

testing1 = file("my_file1")
testing2 = file("my_file2")



# In[ ]:




