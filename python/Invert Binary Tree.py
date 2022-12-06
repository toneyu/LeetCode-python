# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # root.left = root.right
        # root.right = root.left # = root.right = root.right so we would get wrong output
        # we have to update using the old value of a instead of the updated value
    
            # Base case...
        if root == None:
            return root
        # swapping process...
        root.left, root.right = root.right, root.left # required to do single line assignment for swaps
        # Call the function recursively for the left subtree...
        self.invertTree(root.left)
        # Call the function recursively for the right subtree...
        self.invertTree(root.right)
        return root     # Return the root...