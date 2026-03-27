# syntax
'''try:
    # code
except:
    # error handling code'''


# example
try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Error occurred")


# specific exception
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")


# else block
try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Error")
else:
    print("Success")


# finally block
try:
    print("Try block")
except:
    print("Error")
finally:
    print("Always runs")


# multiple exceptions
try:
    a = int(input())
    b = int(input())
    print(a / b)
except (ValueError, ZeroDivisionError):
    print("Error occurred")