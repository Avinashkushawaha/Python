def checkEqualTree(root):
    total = 0
    seen = set()

    def dfs(node):
        nonlocal total
        if not node:
            return 0
        s = node.val + dfs(node.left) + dfs(node.right)
        seen.add(s)
        return s

    total = dfs(root)
    seen.remove(total)
    return total % 2 == 0 and total // 2 in seen
