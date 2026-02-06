from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        time = 0
        q = deque()
        visited = set()

        count_fresh = 0

        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 2):
                    q.append([i, j])
                    visited.add((i, j))
                if (grid[i][j] == 1):
                    count_fresh += 1

        if (count_fresh == 0):
            return 0

        while len(q) > 0:
            levelSize = len(q)
            time += 1

            for i in range(levelSize):
                curr = q.popleft()
                children = self.get_children(grid, curr)

                for [y, x] in [val for val in children if (val[0], val[1]) not in visited]:
                    visited.add((y, x))
                    q.append([y, x])
                    grid[y][x] = 2
                    count_fresh -= 1

                    if (count_fresh == 0):
                        return time

        return time if count_fresh == 0 else -1

    def get_children(self, grid, curr_coord):
        n = len(grid)
        m = len(grid[0])
        steps = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]

        children = []
        y, x = curr_coord

        for step in steps:
            y_stepped = y + step[0]
            x_stepped = x + step[1]

            if (0 <= y_stepped < n and 0 <= x_stepped < m):
                if (grid[y_stepped][x_stepped] == 1):
                    children.append([y_stepped, x_stepped])

        return children
