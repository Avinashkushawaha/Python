from collections import deque

def zigzag_level_order(root):
    if not root: return []
    res, q, left_to_right = [], deque([root]), True
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.insert(0, node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
        left_to_right = not left_to_right
    return res
