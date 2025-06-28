class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, i, j):
        return self.prefix[j+1] - self.prefix[i]

arr = NumArray([-2, 0, 3, -5, 2, -1])
print(arr.sumRange(0, 2))  # 1
