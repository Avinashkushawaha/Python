from functools import lru_cache

class Solution:
    def maximumANDSum(self, nums, numSlots):
        @lru_cache(None)
        def dp(i, state):
            if i == len(nums):
                return 0
            res = 0
            for j in range(numSlots):
                if (state >> (j * 4)) & 0xF < 2:
                    new_state = state + (1 << (j * 4))
                    res = max(res, (nums[i] & (j+1)) + dp(i+1, new_state))
            return res
        return dp(0, 0)
