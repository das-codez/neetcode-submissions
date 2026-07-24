class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(first, i):
            if (i == (len(nums) - 1)) and first:
                return 0
            elif i == (len(nums) - 1):
                return nums[-1]
            elif i >= len(nums):
                return 0
            
            if (first, i) in memo:
                return memo[(first, i)]
            memo[(first, i)] = max(nums[i] + dp(first, i + 2), dp(first, i + 1))
            return memo[(first, i)]
        memo = {}
        return max(dp(True, 0), dp(False, 1))