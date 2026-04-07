# multilevel inheritance
class Grandparent:
    def show_grandparent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am Parent")

class Child(Parent):
    def show_child(self):
        print("I am Child")

obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()


# hierarchical inheritance
class Parent:
    def show_parent(self):
        print("I am Parent")

class Child1(Parent):
    def show_child1(self):
        print("I am Child1")

class Child2(Parent):
    def show_child2(self):
        print("I am Child2")

obj1 = Child1()
obj2 = Child2()

obj1.show_parent()
obj2.show_parent()


# hybrid inheritance
class A:
    def show_A(self):
        print("Class A")

class B(A):
    def show_B(self):
        print("Class B")

class C(A):
    def show_C(self):
        print("Class C")

class D(B, C):
    def show_D(self):
        print("Class D")

obj = D()
obj.show_A()
obj.show_B()
obj.show_C()
obj.show_D()