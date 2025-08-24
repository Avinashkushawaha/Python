class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.key = key

def is_balanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        if left == -1: return -1
        right = height(node.right)
        if right == -1: return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
    return height(root) != -1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(is_balanced(root))  # ✅ True
