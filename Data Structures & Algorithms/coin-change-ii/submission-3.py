class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        def dp(curr, i):
            if i >= len(coins):
                return 0
            if curr == amount:
                return 1
            
            if (curr, i) in memo:
                return memo[(curr, i)]
            
            ans = 0
            if (amount - curr) >= coins[i]:
                ans = dp(curr, i + 1)
                ans += dp(curr + coins[i], i)
            memo[(curr, i)] = ans
            return ans
        memo = {}
        return dp(0, 0)