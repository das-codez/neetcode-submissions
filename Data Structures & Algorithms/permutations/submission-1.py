class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, seen):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    curr.append(nums[i])
                    backtrack(curr, seen)
                    curr.pop()
                    seen.remove(nums[i])
        ans = []
        backtrack([], set())
        return ans
