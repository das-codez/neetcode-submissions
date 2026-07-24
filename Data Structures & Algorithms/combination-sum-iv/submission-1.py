class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1
        def dp(curr):
            if curr == target:
                return 1
            if curr > target:
                return 0
            
            if curr in memo:
                return memo[curr]
            ans = 0
            for num in nums:
                ans += dp(curr + num)
            memo[curr] = ans
            return ans
        memo = {}    
        ans = 0
        for num in nums:
            ans += dp(num)
        return ans