# syntax
'''[expression for item in iterable]'''


# without list comprehension
nums = [1, 2, 3]
result = []

for x in nums:
    result.append(x * 2)



# with list comprehension
nums = [1, 2, 3, 4]

result = [x * 2 for x in nums]
print(result)


# with if condition
nums = [1, 2, 3, 4, 5]

result = [x for x in nums if x % 2 == 0]
print(result)


# with if-else condition
nums = [1, 2, 3, 4]

result = ["even" if x % 2 == 0 else "odd" for x in nums]
print(result)


# string example
texts = "python"

chars = [text for text in texts]
print(chars)