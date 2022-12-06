class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # first stair number = 1, we will increment this value in each iteration by 1
        # we set while loop n > 0 as our condition to break out of loop and that will return our result
        
        
        stair_num = 1
        res = 0
        
        while n > 0:
            n = n - stair_num 
            stair_num += 1
            if n >= 0:
                res += 1
                
        return res
            
        
        
            
        