#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
3.	Напишіть функцію, яка перевіряє, чи є слово паліндромом та повертає відповідно True чи False. Паліндром - це слово, 
яке однаково читається зліва направо та справа наліво. Наприклад, "випив".
"""

def palindrome(s):
    if s[::-1] == s[0:]:
        return True
    else:
        return False

testing1 = palindrome('madam')
print(testing1)

testing2 = palindrome('nice')
print(testing2)


# In[ ]:




