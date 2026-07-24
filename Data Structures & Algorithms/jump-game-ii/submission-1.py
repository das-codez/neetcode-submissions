class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = l = r = 0
        while r < len(nums) - 1:
            farthest = l
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            ans+=1
        return ans