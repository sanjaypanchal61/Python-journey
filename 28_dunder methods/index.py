# example of  __init__ method

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("jack", 20)
print(s.name, s.age)


# example of __str__ method

class Test:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"student name is {self.name}"

z = Test("roy")
print(z)


# example of __len__ method
 
class Data:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

result = Data([1, 2, 3, 4])
print(len(result))


# example of __getitem__ method
 
class Demo:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

x = Demo([10, 20, 30])
print(x[1])