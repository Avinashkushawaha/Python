import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

print(is_valid_email("avinash@gmail.com"))  # True
print(is_valid_email("avinash@.com"))       # False
