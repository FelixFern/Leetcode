class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        array = [[0 for i in range(n)] for i in range(m)]

        array[0][0] = 1

        if (obstacleGrid[0][0] == 1):
            return 0

        for i in range(m):
            for j in range(n):
                if ((i != 0 or j != 0) and obstacleGrid[i][j] == 0):
                    array[i][j] = array[i - 1][j] + array[i][j - 1]
        return array[m - 1][n - 1]
