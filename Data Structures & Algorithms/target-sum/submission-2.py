class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(curr, i):
            if i == len(nums) and curr == target:
                return 1
            if i >= len(nums):
                return 0
            
            
            
            if (curr, i) in memo:
                return memo[(curr, i)]
            ans = 0
            ans += dp(curr + nums[i], i+1)
            ans+= dp(curr - nums[i], i + 1)
            memo[(curr, i)] = ans
            return ans
        memo = {}
        return dp(0, 0)