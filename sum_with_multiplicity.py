def threeSumMulti(arr, target):
    MOD = 10**9 + 7
    from collections import Counter
    cnt = Counter(arr)
    keys = sorted(cnt)
    ans = 0
    for i, a in enumerate(keys):
        for j in range(i, len(keys)):
            b = keys[j]
            c = target - a - b
            if c < b or c not in cnt: continue
            ca, cb, cc = cnt[a], cnt[b], cnt[c]
            if a == b == c:
                ans += ca*(ca-1)*(ca-2)//6
            elif a == b != c:
                ans += ca*(ca-1)//2 * cc
            elif a < b and b < c:
                ans += ca*cb*cc
            # other equalities covered by order constraints
    return ans % MOD

# print(threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
