x = 4
print(x)

def hello():
    x = 5
    print(f"The lacoal value of x is {x}")
    print(f"Hello developer")

print(f"The global value of x is {x}")
hello()
x = 6
print(f"The global value of x is {x}")    