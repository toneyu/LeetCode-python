class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Strategy: use % 2 to check whether each character in the binary string is a 0 or 1
        # increment our result by 1 everytime we compute 1 in our string which we eventually out the number of 1's in the string
        # do right bitwise shift by 1 onto input string n
        
        res = 0;
        while n > 0:
            res += n % 2
            n = n >> 1
        return res