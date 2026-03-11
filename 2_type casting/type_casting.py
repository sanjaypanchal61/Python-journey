age = "20"
height = 5
marks = 85

new_age = int(age) #convert string to integer
new_marks = str(marks) #convert integer to string
new_height = float(height) #convert interger to float

print(type(age))
print(new_age)
print(type(new_age))


# Implicit Type Conversion
n1 = 10
n2 = 5.5

result = n1 + n2

print(result)
print(type(result))

# Explicit Type Conversion
n3 = "5"
n4 = "3"

n3 = int(n3)
n4 = int(n4)

total = n3 + n4

print("Total:", total)
