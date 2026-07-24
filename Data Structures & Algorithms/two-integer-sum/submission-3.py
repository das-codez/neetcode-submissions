class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in myMap:
                return [myMap[res], i]
            myMap[num] = i
        return []