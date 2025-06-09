import re 

def is_strict_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

print(is_strict_palindrome("A man, a plan, a canal: Panama"))