def majority_element(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num 
        count += 1 if num == candidate else -1
    return candidate

print(majority_element([3, 3, 4, 2, 3, 3, 3]))        