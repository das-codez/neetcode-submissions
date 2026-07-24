class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()

        for i, a in enumerate(nums):
            if a in seen and i > 0:
                continue
            seen.add(a)
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum < 0:
                    l+=1
                elif sum > 0:
                    r-=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
               
            
