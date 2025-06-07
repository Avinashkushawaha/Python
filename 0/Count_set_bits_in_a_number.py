def count_set_bits(n):
    return bin(n).count('1')

print(count_set_bits(13))  # 3 (1101)
