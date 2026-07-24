class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i, cooldown):
            if i >= len(prices):
                return 0
            key = (i, cooldown)
            if key in memo:
                return memo[key]
            ans = dp(i + 1, cooldown)
            if not cooldown:
                ans = max(ans, -prices[i] + dp(i + 1, True))
            else:
                ans = max(ans, prices[i] + dp(i + 2, False))
            memo[key] = ans
            return ans
        memo = {}
        return dp(0, False)