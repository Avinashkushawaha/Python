# check if a password is "Weak", "Medium", or "Strong", criteria: <6 chars(Weak),6-10 chars (Medium), > 10 chars (Strong).
password = "Avin123@#1"

password_length = len (password)

if len(password) < 6:
    strength = "Weak"

elif len(password) <= 10:
     strength = "Medium"

else :
     strength = "Strong" 

print("Password strength is: ", strength)
                   