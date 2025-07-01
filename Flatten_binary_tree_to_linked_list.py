def flatten(root):
    if not root: return
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        if stack:
            curr.right = stack[-1]
        curr.left = None
