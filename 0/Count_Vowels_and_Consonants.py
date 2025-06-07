def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = c = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1
    return v, c

print(count_vowels_consonants("Avinash123!"))  # (3, 4)
