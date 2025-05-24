from collections import Counter

def first_non_repeating_char(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

print(first_non_repeating_char("aabbcddee"))  # c
