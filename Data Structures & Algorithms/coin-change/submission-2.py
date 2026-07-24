class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            ans = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    ans = min(ans, 1 + dp(i - coin))
            memo[i] = ans
            return ans
        memo = {0: 0}
        dp(amount)
        return memo[amount] if memo[amount] != float('inf') else -1