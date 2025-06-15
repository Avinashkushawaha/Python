def merge_lists(l1, l2):
    i = j = 0
    result = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result += l1[i:] + l2[j:]
    return result

print(merge_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]   