# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # Solution 1
        # set 3 cases
        # 1. both tree roots are null
        # 2. either tree p or tree q is null
        # 3. any of the values are not equal
        # 4. return the recursive dfs function of both p and q
        
#         if not p and not q: # both trees are null
#             return True
#         if not p or not q or p.val != q.val: # one of the trees are null or values are not equal
#             return False
        
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) # these both need to be true 
    
        # Solution 2
        # 2 cases
        # 1. both tree roots are null
        # 2. both tree roots exists and values are equal
        
        if not p and not q: # if both roots are null
                return True
            
        if p and q and p.val == q.val: # if both roots exist and values are equal return recursive dfs algorithm
                return (self.isSameTree(p.left, q.left) and
                        self.isSameTree(p.right, q.right))
            
        return False
    