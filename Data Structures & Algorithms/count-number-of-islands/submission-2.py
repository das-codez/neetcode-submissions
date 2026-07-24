class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            if not valid(r, c) or grid[r][c] == "0" or (r, c) in seen:
                return
            seen.add((r, c))
            for dr, dc in dirs:
                new_row, new_col = r + dr, c + dc
                dfs(new_row, new_col)
        ans = 0
        seen = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in seen:
                    ans+=1
                    dfs(r, c)
                    seen.add((r, c))
        return ans