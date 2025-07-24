def isIdealPermutation(nums):
    for i, v in enumerate(nums):
        if abs(i - v) > 1:
            return False
    return True
