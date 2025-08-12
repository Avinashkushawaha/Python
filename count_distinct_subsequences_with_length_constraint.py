def countSubseqWithLength(s, k):
    from itertools import combinations
    return len(set(''.join(p) for p in combinations(s, k)))

print(countSubseqWithLength("abcabc", 3))
