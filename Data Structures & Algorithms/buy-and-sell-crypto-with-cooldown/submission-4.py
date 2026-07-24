class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(hold, i):
            if i >= len(prices):
                return 0
            if (hold, i) in memo:
                return memo[(hold, i)]
            
            skip = dp(hold, i + 1)
            if hold:
                sell = dp(False, i + 2) + prices[i]
                memo[(hold, i)] = max(sell, skip)
            else:
                buy = dp(True, i + 1) - prices[i]
                memo[(hold, i)] = max(buy, skip)
            return memo[(hold, i)]
        
        
        return dp(0, False)
        