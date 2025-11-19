# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node1, node2)-> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val==node2.val:
            left=self.helper(node1.left,node2.right)
            right=self.helper(node1.right, node2.left)
            return left and right
        else:
            return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
        