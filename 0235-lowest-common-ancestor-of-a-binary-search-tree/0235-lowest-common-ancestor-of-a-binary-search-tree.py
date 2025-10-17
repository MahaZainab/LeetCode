# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        temp=root
        while temp:
            if temp.val> p.val and temp.val>q.val:
                temp=temp.left
            elif temp.val< p.val and temp.val<q.val:
                temp=temp.right
            else:
                return temp
        return None 
        