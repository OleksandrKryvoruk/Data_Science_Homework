#!/usr/bin/env python
# coding: utf-8

# In[162]:


"""
4.	Напишіть функцію, яка роздруковує всі файли та каталоги поточного каталогу, а також їх кількість окремо. Назви каталогів 
повинні мати позначення"|"
"""
import os
import os.path

def files():
    now_path = os.getcwd()
    count = os.listdir(path=f'{now_path}')
    print(f'PATH - {now_path}, QUANTITY - {len(count)}, FILES - {count}')
    counter = 0
    for i in count:
        choice = os.path.isdir(f"{i}")
        if choice == True:
            counter += 1
            print(f'CATALOGUE - |{i} QUANTITY - {counter}')

testing1 = files()




# In[ ]:




