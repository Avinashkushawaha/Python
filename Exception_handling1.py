try:
    a = 10
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("This will execute no matter what")    