class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_max = curr_min = 1
        for num in nums:
            temp = curr_max * num
            curr_max = max(num, num * curr_max, num * curr_min)
            curr_min = min(num, num * curr_min, temp)
            ans = max(ans, curr_max)
        return ans