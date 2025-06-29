def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x *= sign
    rev = int(str(x)[::-1])
    return sign * rev if rev < 2**31 else 0

print(reverse_integer(123))     # 321
print(reverse_integer(-123))    # -321
