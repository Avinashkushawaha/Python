# find fibbonacci number in python using recursion
def fibbonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)    
print(fibbonacci(10))
    