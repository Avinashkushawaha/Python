a = input("Enter the number: ")
print(f"Multiplication of {a}  is: ")
try:
  for i in range(1, 11):
    print(f'{a} * {i} = {a*i}')
except:
    print("Please enter a valid number")
print('some imp lines of code ')
print("End of the program")
