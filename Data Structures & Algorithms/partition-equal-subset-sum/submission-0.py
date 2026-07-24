class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2


        for num in nums:
            nextDp = set()
            for t in dp:
                if (t + num) == target:
                    return True
                nextDp.add(t + num)
                nextDp.add(t)
            dp = nextDp
        return False