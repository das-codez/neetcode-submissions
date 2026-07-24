class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = {}
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        def dfs(r, c):
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            ans = 1
            for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                
                if valid(nr, nc) and matrix[r][c] < matrix[nr][nc]:
                    ans = max(ans, 1 + dfs(nr, nc))

            dp[(r, c)] = ans
            return dp[(r, c)]
        for r in range(m):
            for c in range(n):
                dfs(r, c)
        return max(dp.values())