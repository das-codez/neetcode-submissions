class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(index):
            if index <= 0:
                return 0
            if index <= 2:
                return index
            if index in memo:
                return memo[index]
            ans = dp(index - 1) + dp(index - 2)
            memo[index] = ans
            return ans
        return dp(n)