def find_pairs(arr, target):
    pairs = []
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    return pairs

print(find_pairs([1, 2, 3, 4, 5], 5))  # [(4, 1), (3, 2)]     
