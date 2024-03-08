class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i != 0 or j != 0):
                    b = grid[i - 1][j]
                    t = grid[i][j - 1]
                    if (j == 0):
                        grid[i][j] += b
                    elif (i == 0):
                        grid[i][j] += t
                    else:
                        grid[i][j] += (t >= b) * b + (b > t) * t
        return grid[-1][-1]
