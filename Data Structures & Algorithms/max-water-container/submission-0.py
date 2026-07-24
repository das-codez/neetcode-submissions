class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            res = max(res, width*height)

            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return res
