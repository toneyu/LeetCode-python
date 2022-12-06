# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # use 2 parameters, [true/false if balanced(bool), current height of subtree(int)]
        
        def dfs(root):
            if not root: return[True, 0] # return true because empty root is balanced and height is 0
            
            left, right = dfs(root.left), dfs(root.right) # determine if from, the left subtree and right subtree whether it is balanced
            balanced = (left[0] and right[0] and # if the left and right subtree are balanced
                       abs(left[1] - right[1]) <= 1) # formula to determine if tree is balanced from the root
            
            return [balanced, 1 + max(left[1], right [1])] # balanced = is the entire tree balanced at all?
        
        return dfs(root)[0]