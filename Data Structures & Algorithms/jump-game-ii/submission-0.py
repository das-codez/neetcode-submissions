class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        min_jump = [float('inf')] * len(nums)
        min_jump[len(nums) - 1] = 0
        for i in range(len(nums) - 2, -1, -1):
            
            for j in range(1, nums[i] + 1):
                if (i + j) < len(nums):
                    min_jump[i] = min(min_jump[i], 1 + min_jump[i+j])
        return min_jump[0]
