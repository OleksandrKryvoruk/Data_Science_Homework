"""
7.	За допомогою Python розрахуйте кількість бітів у кілобайті.
"""
kilobite = int(input("Enter the kilobites "))
bits = kilobite * 1024 * 8
print(f'{kilobite} kilobites = {bits} bits')