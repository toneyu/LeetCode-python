class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # find local min and search for local max, sliding window
        # 2 pointers l = day to buy, r = day to sell
        # the profit is the max - min 
        # 
        l, r = 0, 1 # left = 0, r = 1
        maxP = 0
        
        while r < len(prices): # because we will always be looking to shift our second pointer r until end of prices array
            if prices[l] < prices[r]: # if value on left pointer is less than right pointer AKA if profitable
                profit = prices[r] - prices[l] #calculate the difference of r - l
                maxP = max(maxP, profit) # maxP will be assigned the new max profit if there is a new max profit
            else:
                l = r # in the case the right is ever less than the left, we will move the pointer to the right as the new low 
            r += 1 #continue traversing the rest of the list
        return maxP
        
        
        