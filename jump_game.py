def can_jump(nums):
    goal = len(nums) - 1
    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0

print(can_jump([2,3,1,1,4]))  # True
