class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def findMaximumXOR(self, nums):
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        max_xor = 0
        for num in nums:
            node = root
            curr_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opp = 1 - bit
                if opp in node.children:
                    curr_xor |= (1 << i)
                    node = node.children[opp]
                else:
                    node = node.children[bit]
            max_xor = max(max_xor, curr_xor)
        return max_xor

print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))  # Output: 28
