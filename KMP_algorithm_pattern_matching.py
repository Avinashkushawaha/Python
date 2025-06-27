def kmp_search(text, pattern):
    def build_lps(pat):
        lps = [0] * len(pat)
        length = 0
        i = 1
        while i < len(pat):
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == len(pattern):
            return i - j  # Match found
        elif i < len(text) and text[i] != pattern[j]:
            j = lps[j - 1] if j > 0 else 0
    return -1

print(kmp_search("abxabcabcaby", "abcaby"))  # 6
