#!/usr/bin/env python
# coding: utf-8

# In[146]:


"""
2.	Напишіть функцію, яка отримує словник та назву у рядку, а потім створює файл з цією назвою, який містить всі дані з 
цього словника. Один рядок — одна пара ключ:значення.
"""

def file(*args, **kwargs):
    
    with open(f'{args}.txt', "w") as fq:
        show = fq.write(str(kwargs))

testing1 = file("my_file1", key="my friends")
testing2 = file("my_file2", key="my friend")



# In[ ]:




