class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            ans = 1
            for dr, dc in dirs:
                new_row, new_col = i + dr, j + dc
                if valid(new_row, new_col) and matrix[new_row][new_col] > matrix[i][j]:
                    ans = max(ans, 1 + dp(new_row, new_col))
            memo[(i, j)] = ans
            return ans
            
        ans = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans = max(ans, dp(row, col))
        return ans