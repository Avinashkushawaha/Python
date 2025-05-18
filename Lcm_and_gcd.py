import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(gcd(12, 18))
print(lcm(12, 18))