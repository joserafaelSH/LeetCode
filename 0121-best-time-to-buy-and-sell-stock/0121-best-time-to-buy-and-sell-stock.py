class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0

        while sell < len(prices):

            if prices[buy] < prices[sell]:
                prof = prices[sell]  - prices[buy]
                maxProfit = max(maxProfit, prof)
            else:
                buy=sell
            
            sell+=1
        
        return maxProfit
        