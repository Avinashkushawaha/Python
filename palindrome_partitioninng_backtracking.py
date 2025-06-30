def partition(s):
    res = []

    def is_palindrome(s):
        return s == s[::-1]

    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start+1, len(s)+1):
            if is_palindrome(s[start:end]):
                backtrack(end, path + [s[start:end]])

    backtrack(0, [])
    return res

print(partition("aab"))  # [["a","a","b"],["aa","b"]]
