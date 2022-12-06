class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #declare left and right pointer as 0 and string length - 1 respectively
        #change s to lower case because we ignore cases
        #set condition in while loop to l < r as we compare left and right side strings
        #if left pointer is not alphanumeric continue shifting right
        # if right pointer is not alphanumeric continue shifting left
        # if left is not equal to right at any point return false
        # else continue moving both pointers
        l = 0
        r = len(s)- 1
        s = s.lower()
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l] != s[r]:
                    return False
                else:
                    l+=1
                    r-=1
                    
        return True
                
        