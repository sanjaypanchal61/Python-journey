# operator overloading
# example 1
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return f"total pages: {self.pages}"

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)

# example 2
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

n1 = Number(10)
n2 = Number(20)

result = n1 + n2
print(result)


# method overriding

class Parent:
    def show(self):
        print("this is parent class")

class Child(Parent):
    def show(self):
        print("this is child class")

obj = Child()
obj.show()

# with super()

class Parent:
    def show(self):
        print("parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("child method")

obj = Child()
obj.show()