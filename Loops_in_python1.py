# Calculate the sum of even numbers up to a given numbers n.
n = 10 
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += 1

print("Summ of even number is: ",sum_even)        