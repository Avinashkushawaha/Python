# find foactorial of a number in python using recursion
def factorial(n):
    # if n == 0:
    # if n == 1:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))
