def count_smaller(nums):
    res = []
    sorted_list = []

    def insert(x):
        from bisect import bisect_left, insort
        i = bisect_left(sorted_list, x)
        insort(sorted_list, x)
        return i

    for num in reversed(nums):
        res.append(insert(num))
    return res[::-1]

print(count_smaller([5,2,6,1]))  # [2,1,1,0]
