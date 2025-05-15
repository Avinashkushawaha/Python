# write a program to print multiplication table of a given number using goe loop.
# n = int(input("Enter a number here: ")) 
# for i in range(1, 11):
#     print(f" {n} X {i} = {n * i}")

# write a program to greet all the person names stored in a list "l" and which starts with S.
# l = ["Harry", "Sohan", "Sachin", "Rahul"]

# for name in l:
#     if (name.startswith("S")):
#         print(f"Hello {name}")


# n = int(input("Enter a number: "))
# i = 1

# while(i<11):
#     print(f" {n} X {i} = {n * i}")

#     i+= 1


# n = int(input("Enter a number: "))

# for i in range(2, n):
#     if (n%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")    


# n = int(input("Enter a number here :"))
# product = 1
# for i in range(1, n+1):
#     product = product * i

# print(f"the factorials of {n} is {product}")      

# n = int(input("Enter a number here: "))
# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")
  

# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"* n, end="")
#     else:
#         print("*", end="")
#         print(" "* (n-2), end="")
#         print("*", end="")

#     print("")        


n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")
