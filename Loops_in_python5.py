# Compute the factorial of a number using a while loop.
number = 5
fact = 1

while number > 0:
    # fact = fact * number
    fact *= number 
    number -= 1

print("Factorials number value is :", fact)

