class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            if target in dp: return True
            tmp = set()
            for t in dp:
                tmp.add(t + nums[i])
                tmp.add(t)
            dp = tmp
        return True if target in dp else False