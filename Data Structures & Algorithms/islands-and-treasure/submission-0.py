class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] != -1
        def bfs(row, col):
            q = deque()
            q.append((row, col, row, col, 0))
            seen = set()
            seen.add((row, col))
            while q:
                orig_row, orig_col, curr_row, curr_col, dist = q.popleft()
                
                if grid[curr_row][curr_col] == 0:
                    grid[orig_row][orig_col] = min(grid[orig_row][orig_col], dist)
                for dr, dc in dirs:
                    new_row, new_col = curr_row + dr, curr_col + dc
                    if valid(new_row, new_col) and (new_row, new_col) not in seen:
                        seen.add((new_row, new_col))

                        q.append((orig_row, orig_col, new_row, new_col, dist + 1))
        m = len(grid)
        n = len(grid[0])
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for row in range(m):
            for col in range(n):
                if valid(row, col):
                    bfs(row, col)