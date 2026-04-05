# class create
class Student:
    pass


# object create
s1 = Student()


# constructor
class Demo:
    def __init__(self, name):
        self.name = name

s2 = Demo("jack")
print(s2.name)


# variables
class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# methods
class Student:
    def demo(self):
        print("hello")


# example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

data = Student("roy", 20)
data.show()
