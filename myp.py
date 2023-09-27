try:
    a = int(input("Enter any no:"))
    b = int(input("Enter any no:"))
    c = a / b
    print("Division is ", c)
except ZeroDivisionError:
    print("Not allowed to divide by zero")
except Exception:
    print("Invalid input", Exception)


print("This is awesome")