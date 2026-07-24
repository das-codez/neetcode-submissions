class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ans = 0
        while l < r:
            dist = r - l 
            ans = max(ans, min(heights[r], heights[l]) * dist)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return ans