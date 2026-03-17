# syntax
'''def function_name():
    statement'''


# example
def demo():
    print("Hello world")

demo()


# function with parameters
def demo2(name):
    print("Hello", name)

demo2("jack")


# function with return value
def add(a, b):
    return a + b

result = add(5, 2)
print(result)


# default parameters
def demo3(name="user"):
    print("Hello", name)

demo3()
demo3("jack")


# keyword arguments
def student(name, age):
    print(name, age)

student(age=20, name="jack")

