class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n) for _ in range(m)]
        dp[0][0] = 1 if not obstacleGrid[0][0] else 0
        
            
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if i:
                        dp[i][j]+=dp[i - 1][j]
                    if j:
                        dp[i][j]+=dp[i][j - 1]
                    
        return dp[m - 1][n - 1]