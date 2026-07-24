class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, l = float('inf'), 0
        curr = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                ans = min(r - l + 1, ans)
                curr-=nums[l]
                l+=1
        return ans if ans != float('inf') else 0