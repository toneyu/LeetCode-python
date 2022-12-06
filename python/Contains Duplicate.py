class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # use hashset or list, we check if element is in set then return true
        # we will have to iterate input integer array
        # we have to check first before adding it to set
        
        numberset = set()
        # numberlist = []
        
        for num in nums:
            if num in numberset:
                return True
            else:
                numberset.add(num)
        return False
                
                    
        