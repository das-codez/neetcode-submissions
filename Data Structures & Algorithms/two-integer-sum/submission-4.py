class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for i, num in enumerate(nums):
            index = target - num
            if index in counts:
                return [counts[index], i]
            counts[num] = i
        return