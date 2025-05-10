def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

text = "Avinash"
vowel_count = count_vowels(text)
print(f"Number of vowels in '{text}'is: {vowel_count}")







