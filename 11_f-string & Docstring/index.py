# without f-string
name = "jack"
age = 20

print(f"My name is" , name , "and I am" , age , "years old")


# with f-string
name = "jack"
age = 20

print(f"My name is {name} and I am {age} years old")


#expression in f-string
a = 10
b = 5

print(f"Sum is {a + b}") 


# formatting example
price = 99.4869

print(f"Price: {price:.2f}")


# Docstring

# function Docstring
def add(x, y):
    """This function returns the sum of two numbers"""
    return x + y

print(add(2, 5))

# access Docstring
print(add.__doc__)