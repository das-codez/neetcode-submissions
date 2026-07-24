class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1


        for i in range(len(nums)):
            nextDp = defaultdict(int)
            for curSum, count in dp.items():
                nextDp[curSum + nums[i]] += count
                nextDp[curSum - nums[i]] += count
            dp = nextDp
        return dp[target]