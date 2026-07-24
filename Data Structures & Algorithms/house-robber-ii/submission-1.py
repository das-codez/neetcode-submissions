class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(i,flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if (i, flag) in memo:
                return memo[(i, flag)]
            memo[(i, flag)] = max(nums[i] + dp(i + 2, flag), dp(i + 1, flag))
            return memo[(i, flag)]
        memo = {}
        return max(dp(0, True), dp(1, False))