# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    nullSym = 'N'
    delimiter = ','

    def serialize(self, root):
        """Encodes a tree to a single string."""
        vals = []

        def helper(node):
            if not node:
                vals.append(self.nullSym)
                return
            vals.append(str(node.val))
            helper(node.left)
            helper(node.right)

        helper(root)
        return self.delimiter.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        vals = iter(data.split(self.delimiter))

        def helper():
            val = next(vals)
            if val == self.nullSym:
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        return helper()
