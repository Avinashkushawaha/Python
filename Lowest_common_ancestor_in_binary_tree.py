def lca(root, p, q):
    if not root or root == p or root == q:
        return root 
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    return root if left and right else left or right