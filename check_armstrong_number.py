def is_armstrong_number(n):
    num_str = str(n)
    num_digit = len(num_str)
    return sum(int(digit) ** num_digit for digit in num_str) == n

print(is_armstrong_number(153))
print(is_armstrong_number(123))
                     
                     