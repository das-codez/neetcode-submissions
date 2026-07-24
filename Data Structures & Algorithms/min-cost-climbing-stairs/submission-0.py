class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = min(cost[i] + dp(i + 1), cost[i] + dp(i + 2))
            return memo[i]
        memo = {}
        return min(dp(0), dp(1))