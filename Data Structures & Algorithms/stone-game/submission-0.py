class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        goal = sum(piles) // 2
        def dp(i, j):
            if i >= j:
                return 0
            # if i >= len(piles) or j <= 0:
            #     return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            take_start = piles[i] + max(dp(i + 2, j), dp(i + 1, j - 1))
            take_end = piles[j] + max(dp(i, j - 2), dp(i + 1, j - 1))
            memo[(i, j)] = max(take_start, take_end)
            return memo[(i, j)]

        memo = {}
        return dp(0, len(piles) - 1) > goal
