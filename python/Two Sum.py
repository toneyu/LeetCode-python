class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # goal is to do in one pass to guarantee o(n) solution
        # we need to find two numbers a, b so a + b = target
        # we need to create a hashmap data structure to store the elements we have previously traversed, name it seen = {}
        # the idea is that we iterate b as each element in nums array, we check if we found a (where a = target - b) in the past.
        # if a exists in seen(our hashmap storing elements), then we already found 2 numbers a and b, so we just output their indices.
        # else add b to the seen hashmap
       
        
        seen = {}
        for i, n in enumerate(nums):
            a = target - n
            if a in seen: #if we find a in the array
                return [seen[a], i] # return index of a and index of n
            seen[n] = i #continue updating hashmap for element n
        
        