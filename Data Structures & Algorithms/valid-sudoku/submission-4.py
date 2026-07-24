class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        cols = defaultdict(set)
        for r in range(9):
            rows = set()
            for c in range(9):
                
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows 
                    or board[r][c] in cols[c] 
                    or board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows.add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True