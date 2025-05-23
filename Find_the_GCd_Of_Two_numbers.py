def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("The GCD of 48 and 18 is:", gcd(48, 18))