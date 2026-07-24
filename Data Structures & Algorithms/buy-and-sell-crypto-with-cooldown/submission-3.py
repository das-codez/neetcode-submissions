class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            skip = dp(i + 1, holding)
            if holding:
                sell = dp(i + 2, not holding) + prices[i]
                memo[(i, holding)] = max(sell, skip)
            else:
                buy = dp(i + 1, not holding) - prices[i]
                memo[(i, holding)] = max(buy, skip)
            return memo[(i, holding)]
        return dp(0, False)