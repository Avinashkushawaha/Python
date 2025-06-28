def majority_element(nums):
    if not nums:
        return []
    candidate1 = candidate2 = None
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums)//3]

print(majority_element([3,2,3]))  # [3]
