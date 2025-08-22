from collections import defaultdict

def subarraysWithKDistinct(nums, K):
    def atMost(k):
        count = defaultdict(int)
        res = i = 0
        for j, x in enumerate(nums):
            if count[x] == 0:
                k -= 1
            count[x] += 1
            while k < 0:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    k += 1
                i += 1
            res += j - i + 1
        return res
    return atMost(K) - atMost(K-1)

print(subarraysWithKDistinct([1,2,1,2,3], 2))
