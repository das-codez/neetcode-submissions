class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counts = {}
        ans = 1
        nums.sort()
        for num in nums:
            if (num - 1) in counts:
                curr = counts[num - 1] + 1
                ans = max(ans, curr)
                counts[num] = curr
            else:
                counts[num] = 1
        return ans