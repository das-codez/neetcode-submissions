class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            ans.append(curr[:])
            if i == len(nums):
                return 
            
            for index in range(i, len(nums)):
                curr.append(nums[index])
                backtrack(curr, index + 1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans
