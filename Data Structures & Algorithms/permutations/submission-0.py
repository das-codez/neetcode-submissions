class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, seen):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                if nums[i] not in seen:
                    curr.append(nums[i])
                    seen.add(nums[i])
                    backtrack(curr, seen)
                    seen.remove(nums[i])
                    curr.pop()
        ans = []
        backtrack([], set())
        return ans