import heapq

def merge_k_lists(lists):
    min_heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l[0], i, 0))
    result = []
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
    return result

print(merge_k_lists([[1, 4, 5], [1, 3, 4], [2, 6]]))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]                