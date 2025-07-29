def checkPossibility(nums):
    changed = False
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if changed:
                return False
            changed = True
            if i >= 2 and nums[i] < nums[i - 2]:
                nums[i] = nums[i - 1]
            else:
                nums[i - 1] = nums[i]
    return True
