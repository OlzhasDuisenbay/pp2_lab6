"""Write a Python program with builtin function that returns True
if all elements of the tuple are true."""
def my_func(t):
    return all(t)
t = (True,True,True)
print(my_func(t))
