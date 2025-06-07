def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

print(power(2, 4))  # 16
