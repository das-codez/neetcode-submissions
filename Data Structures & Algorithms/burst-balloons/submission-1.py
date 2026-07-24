class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def dp(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            memo[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dp(l, i - 1) + dp(i + 1, r)
                memo[(l, r)] = max(memo[(l, r)], coins)
            return memo[(l, r)]

        memo = {}
        nums = [1] + nums + [1]
        return dp(1, len(nums) - 2)