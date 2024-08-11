class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        size = len(grid)

        for i in range(size - 2):
            res.append([])
            for j in range(size - 2):
                res[i].append(
                    max([grid[i + ((k // 3) % 3)][j + ((k % 3) % 3)] for k in range(9)]))

        return res
