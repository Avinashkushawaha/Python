from collections import Counter
def longestPalindromeAfterK(s, k):
    freq = Counter(s)
    odd_count = sum(v % 2 for v in freq.values())
    if odd_count <= k:
        return len(s)
    return len(s) - (odd_count - k)

print(longestPalindromeAfterK("abccbaaa", 1))
