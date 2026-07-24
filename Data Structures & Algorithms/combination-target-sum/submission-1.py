class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(curr, index, total):
            if total == target:
                ans.append(curr[:])
                return
            if total > target:
                return
            for i in range(index, len(nums)):
                curr.append(nums[i])
                dfs(curr, i, total + nums[i])
                curr.pop()
        ans = []
        dfs([], 0, 0)
        return ans
            