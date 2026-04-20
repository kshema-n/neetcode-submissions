class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = 0,1
        maxP = 0
        while high < len(prices):
            if prices[low]< prices [high]:
                profit = prices[high] - prices[low]
                maxP = max(maxP, profit)
            else: 
                low = high
            high+=1
        return maxP