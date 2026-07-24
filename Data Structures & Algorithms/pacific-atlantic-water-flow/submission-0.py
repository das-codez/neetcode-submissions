class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        def dfs(row, col, seen):
            nonlocal pacific, atlantic
            if row == 0 or col == 0:
                pacific = True
            if row == m - 1 or col == n - 1:
                atlantic = True
            seen.add((row, col))
            for dr, dc in dirs:
                new_row, new_col = row + dr, col + dc
                if valid(new_row, new_col) and (new_row, new_col) not in seen and heights[new_row][new_col] <= heights[row][col]:
                    dfs(new_row, new_col, seen)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(heights), len(heights[0])
        ans = []
        for row in range(m):
            for col in range(n):
                pacific = False
                atlantic = False
                dfs(row, col, set())
                if pacific and atlantic:
                    ans.append([row, col])

        return ans