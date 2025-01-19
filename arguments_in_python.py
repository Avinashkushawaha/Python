# def average(a, b, c=1):
#     print("The average is ", (a+b+c) / 2)

# average(5, 6)


# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ", sum/ len(numbers))


# average(5, 6, 7, 1)

def name(*name):
    print("Hello,", name["fname"],
   name["mname"], name["lname"])
    
name(mname = "Buchanan", lname = "Barnes",
     fname = "james")    