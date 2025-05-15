# def avg():
#     a = int(input("Enter a number here: "))
#     b = int(input("Enter a number here: "))
#     c = int(input("Enter a number here: "))

#     average =  (a + b + c) / 3
#     print(average)

# avg()    


# def goodDay(name, ending):
#     print("Good Day, " + name)
#     print(ending)

# goodDay('harry', 'thank you')    

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number: "))
print(f"The factorials of this number is: {factorial(n)}")
