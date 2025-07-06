import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val):
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]

kl = KthLargest(3, [4, 5, 8, 2])
print(kl.add(3))  # 4
print(kl.add(5))  # 5
