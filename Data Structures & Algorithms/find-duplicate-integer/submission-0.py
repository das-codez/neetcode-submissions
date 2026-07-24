class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = 0
        curr = nums
        for num in nums:
            mask = 1 << num
            if mask & seen:
                return num
            else:
                seen^=mask
