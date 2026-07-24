class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and board[row][col] == "O"
        def dfs(r, c):
            if not valid(r, c):
                return
            board[r][c] = "T"
            for dr, dc in dirs:
                row, col = r + dr, c + dc
                dfs(row, col)

        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n - 1] == "O":
                dfs(r, n - 1)
        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m - 1][c] == "O":
                dfs(m - 1, c)
            
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
            