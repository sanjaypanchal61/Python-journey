# syntax
'''for variable in sequence:
    statement
else:
    statement'''


# example
for i in range(5):
    print(i)
else:
    print("Loop completed")


# with break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")


# search program
nums = [1, 2, 3, 4, 5]

searchNum = 10

for num in nums:
    if num == searchNum:
        print("Found")
        break
else:
    print("Not Found")


# example – prime number check

num = 7

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")