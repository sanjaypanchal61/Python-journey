# syntax

'''match variable:
    case value1:
        statement
    case value2:
        statement
    case _:
        default statement'''



# example 1
day = 1

match day:
    case 1:
        print("day 1")
    case 2:
        print("day 2")
    case 3:
        print("day 3")
    case _:
        print("invalid day")


# example 2
num = int(input("enter a number:"))

match num:
    case 1:
        print("you entered one")
    case 2:
        print("you entered two")
    case 3:
        print("you entered three")
    case _:
        print("invalid number")
