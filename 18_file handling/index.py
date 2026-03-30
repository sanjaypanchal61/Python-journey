# file open
file = open("demo.txt", "r")


# file read
content = file.read()
print(content)
file.close()


# file write
file = open("demo.txt", "w")
file.write("hello world")
file.close()


# file append
file = open("demo.txt","a")
file.write("hello python")
file.close()


# with statement
with open("demo.txt", "r") as file:
    print(file.read())