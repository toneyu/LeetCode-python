class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # we set left and right pointer to l = 0 and r = length of input array - 1
        # set a while loop for left <= right to search until index target is found || set to < than if r = len(nums)
        # set middle to l + r divided by 2
        # if the value in the middle is greater than our target input, then that means we must search the left side of sorted array
        # vice versa, we will search the right side of sorted array if input target is greater than middle value
        # return mid if 
        r = len(nums) - 1 
        l = 0
        while(l <= r):
            mid = (l + r)//2
            if nums[mid] > target: #if value in middle is greater than input target 
                r = mid - 1 # the right side of the subarray is middle index - 1
            elif nums[mid] < target: # if middle value is less than input target
                l = mid + 1 # the left side of the subarray is middle index + 1
            else:
                return mid # return mid index # if target is in middle
        return -1

        
    
        