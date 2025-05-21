# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end='')
#         a, b = b, a + b

# fibonacci(10)        

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=' ')