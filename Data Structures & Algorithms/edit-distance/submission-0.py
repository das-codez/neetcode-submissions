class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        first, second = len(word1), len(word2)
        dp = [[float('inf')] * (second + 1) for i in range(first + 1)]
        for j in range(second + 1):
            dp[first][j] = second - j
        for i in range(first + 1):
            dp[i][second] = first - i

        for i in range(first - 1, -1, -1):
            for j in range(second - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]