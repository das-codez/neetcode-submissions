class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in counts:
                return [counts[val], i]
            counts[num] = i
        return