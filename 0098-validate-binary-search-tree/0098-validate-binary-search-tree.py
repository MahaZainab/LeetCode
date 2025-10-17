# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root, listv):
        if not root:
            return
        self.inorder(root.left, listv)
        listv.append(root.val)
        self.inorder(root.right,listv)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        listv=[]
        self.inorder(root, listv)
        for i in range(1, len(listv)):
            if listv[i]<=listv[i-1]:
                return False
        return True

        