def sum_of_number(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_number(123))