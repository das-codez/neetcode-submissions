class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(row, col):
            if row == 0 and col == 0:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            ans = 0
            if row - 1 >= 0:
                ans += dp(row - 1, col)
            if col - 1 >= 0:
                ans += dp(row, col -1)
            memo[(row, col)] = ans
            return ans
        memo = {}
        return dp(m - 1, n - 1)