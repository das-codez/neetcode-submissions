class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = val + nums[l] + nums[r]
                if curr > 0:
                    r-=1
                elif curr < 0:
                    l+=1
                else:
                    ans.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l - 1] == nums[l]:
                        l+=1
        return ans