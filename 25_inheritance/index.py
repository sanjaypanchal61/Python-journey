# single inheritance syntax
class Parent:
    pass

class Child(Parent):
    pass


# single inheritance example
class Animal:
    def speak(self):
        print("animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()


# multiple inheritance syntax
class A:
    pass

class B:
    pass

class C(A, B):
    pass


# multiple inheritance example
class Father:
    def skills(self):
        print("Father: Driving")

class Mother:
    def skills(self):
        print("Mother: Teaching")

class Child(Father, Mother):
    def skills(self):
        print("Child: Gaming")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()