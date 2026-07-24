class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zerCnt = 1, 0
        res = [0] * len(nums)
        for num in nums:
            if num == 0:
                zerCnt+=1
            else:
                prod*=num
        if zerCnt > 1:
            return res

        for i, n in enumerate(nums):
            if zerCnt:
                res[i] = 0 if n else prod
            else:
                res[i] = prod // n
        return res
        
        
