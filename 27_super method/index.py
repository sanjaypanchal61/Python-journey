# example
class Parent:
    def show(self):
        print("this is parent class")

class Child(Parent):
    def show(self):
        super().show()   # parent method call
        print("this is child class")

obj = Child()
obj.show()


# with constructor
class Parent:
    def __init__(self, name):
        self.name = name
        print("parent constructor called")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # parent constructor call
        self.age = age
        print("child constructor called")

obj = Child("jack", 20)
print(obj.name, obj.age)


# with multiple inheritance
class A:
    def show(self):
        print("class a")

class B(A):
    def show(self):
        super().show()
        print("class b")

class C(A):
    def show(self):
        super().show()
        print("class c")

class D(B, C):
    def show(self):
        super().show()
        print("class d")

obj = D()
obj.show()