# for loop syntax

'''for variable in sequence:
    statement'''

# example 1
for i in range(10):
    print(i)


# example 2
for num in range(1, 10):
    print(num)


# while loop syntax

'''while condition:
    statement'''

# example 1
i = 1

while i <= 5:
    print(i)
    i += 1


# break statement
for i in range(10):
    if i == 5:
        break
    print(i)


# continue statement
for i in range(5):
    if i == 4:
        continue
    print(i)


# nested loop
for i in range(3):
    for j in range(2):
        print(i, j)