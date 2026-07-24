class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_buy = prices[0]
        for sell in prices:
            ans = max(ans, sell - min_buy)
            min_buy = min(min_buy, sell)
        return ans