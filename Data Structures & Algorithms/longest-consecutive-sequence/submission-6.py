class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            cnt = 0
            while num + cnt in num_set:
                cnt+=1
            longest = max(longest, cnt)

        return longest
