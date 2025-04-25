"""
5.	Напишіть код, який просить ввести дві будь-яких змінних, а 
потім міняє їх місцями.
"""
while True:
    ver1 = input("Enter the ver1 (Enter stop to exit) ")
    ver2 = input("Enter the ver2 (Enter stop to exit) ")
    ver1,ver2 = ver2,ver1
    print(f'ver1 = {ver1} - ver2 = {ver2}')
    break