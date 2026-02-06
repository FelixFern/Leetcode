from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        elif (n == 1):
            return 1

        q = deque()
        q.append([0, 0])

        visited = set()
        visited.add((0, 0))
        curr_path_length = 1

        while len(q) > 0:
            levelSize = len(q)
            curr_path_length += 1

            for i in range(levelSize):
                curr = q.popleft()
                children = self.get_children(grid, curr)

                for j in [val for val in children if (val[0], val[1]) not in visited]:
                    q.append(j)
                    visited.add((j[0], j[1]))

                if ((n - 1, n - 1) in visited):
                    return curr_path_length

        return -1

    def get_children(self, grid, curr_coord):
        n = len(grid)
        steps = [
            [0, 1],
            [1, 0],
            [1, 1],
            [0, -1],
            [-1, 0],
            [-1, -1],
            [-1, 1],
            [1, -1]
        ]

        children = []
        y, x = curr_coord

        for step in steps:
            y_stepped = y + step[0]
            x_stepped = x + step[1]

            if (0 <= y_stepped < n and 0 <= x_stepped < n):
                if (grid[y_stepped][x_stepped] == 0):
                    children.append([y_stepped, x_stepped])

        return children
