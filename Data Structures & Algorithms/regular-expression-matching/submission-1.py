class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dp(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            if (i, j) in memo:
                return memo[(i, j)]
            matching = i < len(s) and (p[j] == "." or s[i] == p[j])
            memo[(i, j)] = False
            if (j + 1) < len(p) and p[j + 1] == "*":
                memo[(i, j)] = dp(i, j + 2) or (matching and dp(i + 1, j))
                return memo[(i, j)]
            
            if matching:
                memo[(i, j)] = dp(i + 1, j + 1)
                return memo[(i, j)]
            return memo[(i, j)]
            
        memo = {}
        return dp(0, 0)