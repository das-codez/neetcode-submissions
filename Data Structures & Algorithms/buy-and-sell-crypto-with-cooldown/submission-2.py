class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i, cool):
            if i >= len(prices):
                return 0
            if (i, cool) in memo:
                return memo[(i, cool)]
            
            skip = dp(i + 1, cool)
            if not cool:
                buy = dp(i + 1, not cool) - prices[i]
                memo[(i, cool)] = max(skip, buy)
            else:
                sell = dp(i + 2, not cool) + prices[i]
                memo[(i, cool)] = max(skip, sell)
            return memo[(i, cool)]
        memo = {}
        return dp(0, False)
