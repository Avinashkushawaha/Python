def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary or "0"

print(decimal_to_binary(10))  # 1010
