class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #   perform binary search on our input num
        #   set two pointers, left = 1, right = our input number
        #   compute the middle value = floor[( left + right)]/2
        #   check if middle squared is less than or greater than num
    # left = mid + 1 indicates the new computed square is smaller, right = mid - 1 indicates it is larger
        # general idea is just to compute the middle, square it and continue computing the square towards the input integer ie to the right if the current number computed is smaller or to the left if the current number computed is larger
        
    
        l = 1           #l, r = 1, num
        r = num
        while l <= r: # input 9, final iteration  3 <= 4
            mid = (l + r)//2  # (1 + 9)//2 = 5 | (1 + 4)//2 = 2  | mid = (3 + 4) //2 = 3
            if mid * mid > num: # 5*5 > 9 = true | 2 * 2 > 9 = false | 3 * 3 = 9 > num =false
                r = mid - 1 # r = 5 - 1 = 4
            elif mid * mid < num:#  2 * 2 < 9 = true | 3 * 3 < 9 = false | 
                l = mid + 1 # l = 2 + 1 = 3
            else:
                return True # both if and elif statements fail on 3rd iteration so we have found our solution 
            
        return False
        
     
         #while l <= r: # input 3 || 2 <= 1 no longer true so exit loop and return false
#             mid = (l + r)//2  # mid = (1 + 3)//2 = 2 | mid = (1 + 2)//2 = 1
#             if mid * mid > num: # 2 * 2 > num = true | 1 * 1 = 1 = false
#                 r = mid - 1 # r = 2 - 1 = 1 | r = 1
#             elif mid * mid < num:#  1 * 1 < num = true
#                 l = mid + 1 # 1 = 1 + 1 = 2 | l = 2
#             else:
#                 return True # n 
            
#         return False

#         for i in range(1, num + 1):
#             if i*i == num:
#                 return True
#             if i*i > num:
#                 return False
    
    
        