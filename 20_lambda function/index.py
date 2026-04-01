# syntax
'''lambda arguments: expression'''


# example
add = lambda a, b: a + b
print(add(5, 3))


# multiple arguments
mul = lambda a, b, c: a * b * c
print(mul(4, 6, 3))


# with if-else
demo = lambda x: "even" if x % 2 == 0 else "odd"
print(demo(10))