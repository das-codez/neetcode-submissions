class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        
        target = total_sum // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]
        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            memo[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return memo[i][target]
        return dfs(0, target)