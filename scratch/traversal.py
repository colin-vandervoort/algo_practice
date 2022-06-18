# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(6)

root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = TreeNode(0)
q = TreeNode(9)

def traverse(root, p, q):
    curr = root
    stack = []
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right
        else:
            break


traverse(root, p, q)