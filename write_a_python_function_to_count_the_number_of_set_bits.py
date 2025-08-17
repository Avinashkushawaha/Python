def count_set_bits(n):
    count = 0
    while n:
        n &= (n - 1)  # Brian Kernighan’s algorithm
        count += 1
    return count

print(count_set_bits(13))  # 3 (1101)
