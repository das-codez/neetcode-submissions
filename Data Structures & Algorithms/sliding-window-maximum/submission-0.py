class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        ans = []
        max_val = max(nums[l:k])
        ans.append(max_val)
        for r in range(k, len(nums)):
            l+=1
            max_val = max(nums[l:r+1])
            ans.append(max_val)
        return ans