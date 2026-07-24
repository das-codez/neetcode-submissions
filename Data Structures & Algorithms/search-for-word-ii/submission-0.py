class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        root = TrieNode()
        for word in words:
            root.add(word)
        m, n = len(board), len(board[0])
        def backtrack(row, col, node, curr):
            if not valid(row, col) or (row, col) in visit or board[row][col] not in node.children:
                return
            visit.add((row, col))
            node = node.children[board[row][col]]
            curr.append(board[row][col])
            if node.word:
                ans.append("".join(curr))
                node.word = False
            for dr, dc in dirs:
                new_row, new_col = row + dr, col + dc
                backtrack(new_row, new_col, node, curr)
            visit.remove((row, col))
            curr.pop()
        ans, visit = [], set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1,0)]
        for row in range(m):
            for col in range(n):
                backtrack(row, col, root, [])
        return ans