class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(cur, i):
            if sum(cur) == target:
                ans.append(cur[:])
            elif sum(cur) > target:
                return
            else:
                for j in range(i, len(nums)):
                    cur.append(nums[j])
                    backtrack(cur, j)
                    cur.pop()
        ans = []
        backtrack([], 0)
        return ans
                    