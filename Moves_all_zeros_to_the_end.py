def move_zeros(nums):
    return [x for x in nums if x != 0] + [0] * nums.count(0)

print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
