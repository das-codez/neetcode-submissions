class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for column in range(9):
                curr = board[row][column]
                if curr == ".":
                    continue
                if(curr in rows[row]
                    or curr in cols[column]
                    or curr in squares[(row//3, column//3)]):
                    return False
                
                rows[row].add(curr)
                cols[column].add(curr)
                squares[(row//3, column//3)].add(curr)
        return True