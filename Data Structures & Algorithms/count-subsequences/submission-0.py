class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            ans = dp(i + 1, j)
            if s[i] == t[j]:
                ans += dp(i + 1, j + 1)
            memo[(i, j)] = ans
            return ans
        memo = {}
        return dp(0, 0)