
def minCameraCover(root):
    cams = 0
    def dfs(node):
        nonlocal cams
        if not node: return 2
        l, r = dfs(node.left), dfs(node.right)
        if l == 0 or r == 0:
            cams += 1
            return 1
        if l == 1 or r == 1:
            return 2
        return 0
    return cams + (dfs(root) == 0)

# build a TreeNode and call minCameraCover(root)
