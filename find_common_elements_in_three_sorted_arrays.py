def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    result = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        else:
            min_val = min(arr1[i], arr2[j], arr3[k])
            if arr1[i] == min_val:i += 1
            if arr2[j] == min_val: j += 1
            if arr3[k] == min_val: k += 1
    return result
           
print(common_elements([1, 5, 10], [1, 4, 10], [1, 10]))           