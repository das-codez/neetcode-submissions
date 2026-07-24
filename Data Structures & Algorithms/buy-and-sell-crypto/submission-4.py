class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_val = float('inf')
        for price in prices:
            ans = max(ans, price - min_val)
            min_val = min(min_val, price)
        return ans
