class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        maxHorizontal = [0 for i in xrange(n)]
        maxVertical = [0 for i in xrange(n)]

        for i in range(n):
            print(grid[i][:])
            maxVertical[i] = max(grid[i][:])
            temp = grid[0][i]

            for j in range(1, n):
                if(grid[j][i] > temp):
                    temp = grid[j][i]
            
            maxHorizontal[i] = temp
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(maxVertical[j], maxHorizontal[i]) - grid[i][j] 

        return res