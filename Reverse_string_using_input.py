input_string = input("Enter String: ")
n = int(input("Enter n:"))

alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets, reverse_alphabets))


prefix = input_string[0:n-1]
suffix = input_string[n-1:]

mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]


res = prefix + mirror
print("The result is:", res)    