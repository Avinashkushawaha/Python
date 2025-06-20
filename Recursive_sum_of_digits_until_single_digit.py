def digit_root(n):
    if n < 10:
        return n
    return digit_root(sum(int(d) for d in str(n)))

print(digit_root(38))  # Output: 2
