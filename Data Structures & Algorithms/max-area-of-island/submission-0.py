class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col]
        def dfs(row, col):
            seen.add((row, col))
            curr = 1
            for dr,dc in dirs:
                next_row, next_col = row+dr, col + dc
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    curr += dfs(next_row, next_col)
            return curr
        m = len(grid)
        n = len(grid[0])
        seen = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        for row in range(m):
            for col in range(n):
                if valid(row, col) and (row, col) not in seen:
                    ans = max(ans, dfs(row, col))
        return ans