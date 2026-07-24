class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        min_prod = max_prod = 1
        for num in nums:
            old_max = max_prod * num
            max_prod = max(num, max_prod * num, min_prod * num)
            min_prod = min(old_max, num, min_prod * num)
            ans = max(ans, max_prod)
        return ans