class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        ans = 0
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            curr = 1

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    curr_row, curr_col = dr + row, dc + col
                    if valid(curr_row, curr_col) and grid[curr_row][curr_col] == 1:
                        q.append((curr_row, curr_col))
                        grid[curr_row][curr_col] = 0
                        curr+=1
            return curr
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, bfs(r, c))
        return ans