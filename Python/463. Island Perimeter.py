grid = [[1]]
perimeter = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        steps = [
            [0, 1], [1, 0], [0, -1], [-1, 0]
        ]
        if grid[i][j] == 1:
            count = 0
            for step in steps:
                if i + step[0] < 0 or i + step[0] >= len(grid) or j + step[1] < 0 or j + step[1] >= len(grid[0]):
                    continue
                elif grid[i + step[0]][j + step[1]] == 1:
                    count += 1
            perimeter += (4 - count)
print(perimeter)
