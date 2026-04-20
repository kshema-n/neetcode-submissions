class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0
        for i in prices:
            minBuy = min(minBuy, i)
            profit = max(profit, i-minBuy)
        return profit