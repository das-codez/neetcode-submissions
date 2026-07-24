class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        def valid(row, col):
            return 0 <= row < n and 0 <= col < m

        def backtrack(row, col, index, seen):
            if index == len(word) - 1 and board[row][col] == word[index]:
                return True
            elif board[row][col] == word[index]:
                seen.add((row, col))
                for dr, dc in dirs:
                    new_row, new_col = row + dr, col + dc
                    if valid(new_row, new_col) and (new_row, new_col) not in seen:
                        if backtrack(new_row, new_col, index + 1, seen):
                            return True
                seen.remove((row,col))
                return False

        n = len(board)
        m = len(board[0])
        dirs = [(0, 1), (0, -1), (1,0), (-1,0)]
        for row in range(n):
            for col in range(m):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0, set()):
                        return True
        return False