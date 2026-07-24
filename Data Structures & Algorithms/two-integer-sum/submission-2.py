class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i,n in enumerate(nums):
            curr = target - n
            if curr in myMap:
                return [myMap[curr], i]
            else:
                myMap[n] = i
        
        return 