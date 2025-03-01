"""Write a Python program with builtin function that accepts a string and
calculate the number of upper case letters and lower case letters"""
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count
str = input("Enter a string:")
upper,lower = count_upper_lower(str)
print("Number of upper case letters:",upper)
print("Number of lower case letters:",lower)
#KBtu
#Number of upper case letters: 2
#Number of lower case letters: 2
