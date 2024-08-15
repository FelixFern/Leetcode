class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        res = [[0 for i in range(n)] for j in range(m)]

        row0 = [0] * m
        row1 = [0] * m
        col0 = [0] * n
        col1 = [0] * n

        for i in range(m):
            for j in range(n):
                row0[i] += grid[i][j] == 0
                col0[j] += grid[i][j] == 0
                row1[i] += grid[i][j] == 1
                col1[j] += grid[i][j] == 1

        for i in range(m):
            for j in range(n):
                res[i][j] = row1[i] + col1[j] - row0[i] - col0[j]
        return res
