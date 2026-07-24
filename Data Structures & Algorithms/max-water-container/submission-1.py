class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        longest = 0
        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            longest = max(curr, longest)
            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return longest