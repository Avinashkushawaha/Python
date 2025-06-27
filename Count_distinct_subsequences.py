def distinct_subseq(s):
    mod = 10**9 + 7
    dp = [1]
    last = {}

    for i, ch in enumerate(s):
        dp.append(dp[-1] * 2 % mod)
        if ch in last:
            dp[-1] = (dp[-1] - dp[last[ch]]) % mod
        last[ch] = i

    return (dp[-1] - 1) % mod

print(distinct_subseq("abc"))  # 7
