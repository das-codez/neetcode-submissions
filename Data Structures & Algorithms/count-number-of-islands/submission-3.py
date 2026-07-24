class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        ans = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + row, dc + col
                    if valid(nr, nc) and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    bfs(r, c)
                    ans+=1
        return ans