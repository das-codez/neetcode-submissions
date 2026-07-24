class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            ans = max(nums[i] + dp(i + 2), dp(i + 1))
            memo[i] = ans
            return ans
        memo = {}
        return dp(0)