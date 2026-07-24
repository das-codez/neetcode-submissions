class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        ans = 0
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if valid(nr, nc) and grid[nr][nc] == "1":
                        bfs(nr, nc)
                        grid[nr][nc] == "0"
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    bfs(row, col)
                    ans+=1
        return ans