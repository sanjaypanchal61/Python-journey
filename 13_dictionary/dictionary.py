# create dictionary
student = {
    "name": "jack",
    "age": 20
}
print(student)

# access
print(student["name"])
print(student.get("age"))

# add/update
student["course"] = "B.A"   # add
student["age"] = 21         # update

# remove elements
student.pop("age")
student.clear()

# loop in dictionary
for key in student:
    print(key, student[key])



# methods
print(student.keys())
print(student.values())
print(student.items())

# nested dictionary
fruits = {
    "fruit1": {"name": "Apple", "color": "red"},
    "fruit2": {"name": "Mango", "color": "green"}
}
print(fruits["fruit1"]["name"])

# dictionary length
print(len(student))
