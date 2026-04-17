# without walrus operator
n = len([1, 2, 3])
if n > 2:
    print(n)



# with walrus operator
if (n := len([1, 2, 3])) > 2:
    print(n)



# user input example
while (data := input("enter you name: ")) != "exit":
    print(f"Your name is: {data}")