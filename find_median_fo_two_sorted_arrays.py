def find_median_sorted_arrays(A, B):
    A, B = sorted(A), sorted(B)
    merged = sorted(A + B)
    n = len(merged)
    mid = n // 2
    return (merged[mid - 1] + merged[mid - 1]) / 2 if n % 2 == 0 else merged[mid]

print(find_median_sorted_arrays([1, 3], [2]))  