from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def subTreeHeight(root: Optional[TreeNode], rootHeight: int) -> int:
            leftHeight = subTreeHeight(root.left, rootHeight + 1) if root.left else rootHeight
            rightHeight = subTreeHeight(root.right, rootHeight + 1) if root.right else rootHeight

            if (abs(leftHeight - rightHeight) > 1):
                return -1
            else:
                return max(leftHeight, rightHeight)

        if root is None:
            return True

        rootHeight = 0
        leftHeight = subTreeHeight(root.left, rootHeight + 1) if root.left else rootHeight
        rightHeight = subTreeHeight(root.right, rootHeight + 1) if root.right else rootHeight

        if leftHeight == -1:
            return False
        if rightHeight == -1:
            return False
        if abs(leftHeight - rightHeight) > 1:
            return False
        return True

