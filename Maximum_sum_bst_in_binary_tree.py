class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def maxSumBST(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return True, float('inf'), float('-inf'), 0
        l_ok, l_min, l_max, l_sum = dfs(node.left)
        r_ok, r_min, r_max, r_sum = dfs(node.right)
        ok = l_ok and r_ok and l_max < node.val < r_min
        if ok:
            s = l_sum + r_sum + node.val
            ans = max(ans, s)
            return True, min(l_min, node.val), max(r_max, node.val), s
        return False, 0, 0, 0
    dfs(root)
    return ans

# Example usage would construct a tree and call maxSumBST(root)
