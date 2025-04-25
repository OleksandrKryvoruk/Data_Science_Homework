"""
3.	Напишіть цикл for, який просить ввести ціле число 10 разів, а потім 
роздруковує у консолі суму всіх введених чисел.
"""
lst = []
for x in range(10):
    numb = int(input("Enter the number "))
    lst.append(numb)
result = sum(lst)
print(result)
