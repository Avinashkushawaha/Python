from functools import reduce
# Map Example 

l = [1, 2, 3, 4, 5]

Square = lambda x: x*x

sqList = map(Square, l)
print(list(sqList))

# Filter Example

def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))
    
 # Reduce Example

def sum(a, b):
    return a + b

print(reduce(sum, l))