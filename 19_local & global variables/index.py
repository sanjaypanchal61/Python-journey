# local variable
def demo():
    x = 10 # local variable
    print(x)

demo()


# global variable
a = 20 # global variable

def test():
    print(a)

test()


# same name variable
b = 50

def test2():
    b = 10
    print(b)

test2()
print(b)


# global keyword
c = 10

def change():
    global c
    c = 20

change()
print(c)