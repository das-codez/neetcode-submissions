class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i <= 1:
                return cost[i]
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dp(i - 1), dp(i - 2))
            return memo[i]
        memo = {}
        return min(dp(len(cost) - 1), dp(len(cost) - 2))