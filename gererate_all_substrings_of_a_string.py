def all_string(s):
    substrs = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrs.append(s[i:j])

    return substrs

print(all_string("abc"))
        