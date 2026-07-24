class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def dp(alice, i, m):
            if i == len(piles):
                return 0
            
            if (alice, i, m) in memo:
                return memo[(alice, i, m)]
            ans = 0 if alice else float('inf')
            total = 0
            for x in range(1, (2 * m) + 1):
                if i + x > len(piles):
                    break
                total += piles[i + x - 1]
                if alice:
                    ans = max(ans, total + dp(not alice, i + x, max(m, x)))
                else:
                    ans = min(ans, dp(not alice, i + x, max(m, x)))
            memo[(alice, i, m)] = ans
            return ans
        memo = {}
        return dp(True, 0, 1)
