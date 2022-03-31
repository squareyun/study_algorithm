class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        
        cols = len(obstacleGrid[0])
        rows = len(obstacleGrid)

        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = 1

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]