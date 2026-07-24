class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numSet:
                index = 1
                
                while (num + index) in numSet:
                    index+=1
                longest = max(index, longest)


        return longest
