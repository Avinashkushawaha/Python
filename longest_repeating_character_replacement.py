def character_replacement(s, k):
    count = {}
    maxf = i = 0
    for j in range(len(s)):
        count[s[j]] = count.get(s[j], 0) + 1
        maxf = max(maxf, count[s[j]])
        if j - i + 1 - maxf > k:
            count[s[i]] -= 1
            i += 1
    return len(s) - i

print(character_replacement("AABABBA", 1))  # 4
