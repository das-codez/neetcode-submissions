class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, diag, anti_diag, vert, board):
            if row == n:
                ans.append(["".join(r) for r in board])
                return
            for col in range(n):
                curr_diag = row - col
                curr_anti_diag = row + col
                if col in vert or curr_diag in diag or curr_anti_diag in anti_diag:
                    continue
                board[row][col] = "Q"
                vert.add(col)
                diag.add(curr_diag)
                anti_diag.add(curr_anti_diag)

                backtrack(row + 1, diag, anti_diag, vert, board)

                board[row][col] = "."
                vert.remove(col)
                diag.remove(curr_diag)
                anti_diag.remove(curr_anti_diag) 
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        backtrack(0, set(), set(), set(), board)
        return ans