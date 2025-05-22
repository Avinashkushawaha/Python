def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

print(is_armstrong(153))  # Output: True
print(is_armstrong(123))  # Output: False