class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"
        def dfs(row,col):
            for dr, dc in dirs:
                new_row, new_col = row + dr, col + dc
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)

        seen = set()
        m = len(grid)
        n = len(grid[0])
        ans = 0
        dirs = [(0, 1), (0, -1), (1,0), (-1,0)]
        for row in range(m):
            for col in range(n):
                if valid(row, col) and (row, col) not in seen:
                    ans+=1
                    seen.add((row, col))
                    dfs(row, col)
        return ans
