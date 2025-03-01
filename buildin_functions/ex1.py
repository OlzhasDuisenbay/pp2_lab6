#Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
n = int(input())
numbers= []
for i in range(n):
    s = int(input("Enter a number:"))
    numbers.append(s)
result = reduce(lambda x, y: x * y, numbers)
print(result)
# [1,2,3,4,5] >> 120
