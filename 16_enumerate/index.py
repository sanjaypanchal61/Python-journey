# without enumerate
fruits = ["apple", "banana", "mango"]

index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1



# with enumerate
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# with start value
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits,start=1):
    print(index, fruit)



# enumerate to list
fruits = ["apple", "banana"]

result = list(enumerate(fruits))
print(result)