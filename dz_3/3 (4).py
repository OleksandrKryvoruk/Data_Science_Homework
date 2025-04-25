"""
4.	Напишіть нескінченний цикл, який просить ввести ціле число і 
переривається, якщо введене число менше 0.
"""
while True:
    numb = int(input("Enter the number "))
    print(numb)
    if numb < 0:
        break
