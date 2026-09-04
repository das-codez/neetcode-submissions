class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def valid(r, c):
            return ((0 <= r < m) and (0 <= c < n))
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))


        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if valid(nr, nc) and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            dist += 1