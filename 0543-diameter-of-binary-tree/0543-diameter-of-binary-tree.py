class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def height(node):
            if not node:
                return 0
            lh=height(node.left)
            rh=height(node.right)
            self.diameter=max(self.diameter, lh+rh)
            return 1+ max(lh,rh)
        height(root)
        return self.diameter

"""# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root)->int:
            if not root:
                return 0
            lh=height(root.left)
            rh=height(root.right)
            return max(lh,rh)+1
        if not root:
            return 0
        leftDiameter=self.diameterOfBinaryTree(root.left)
        leftHeight=height(root.left)
        rightDiameter=self.diameterOfBinaryTree(root.right)
        rightHeight=height(root.right)
        selfDia=leftHeight+rightHeight
        return max(selfDia,max(leftDiameter, rightDiameter))
        """
        