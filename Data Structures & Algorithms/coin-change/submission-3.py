class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if ((i - coin) >= 0 ) and (dp[i - coin] != -1):
                    if dp[i] != -1:
                        dp[i] = min(dp[i], 1 + dp[i - coin])
                    else:
                        dp[i] = dp[i - coin] + 1
        return dp[-1]
