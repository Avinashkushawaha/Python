def num_decodings(s):
    if not s or s[0] == '0':
        return 0 
    dp = [1, 1]
    for i in range(1, len(s)):
        dp.append(0)
        if s[i] != '0':
            dp[-1] += dp[-2]
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            dp[-1] += dp[-3]

    return dp[-1]

print(num_decodings("226"))        