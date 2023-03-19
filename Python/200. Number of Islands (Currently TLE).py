grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
w = len(grid[0])
h = len(grid)
steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]
island = []
n = 0


def checkIsland(i, j):
    if grid[i][j] == "1":
        island.append([i, j])
        for step in steps:
            if ([max(0, min(h - 1, i + step[0])), max(0, min(w - 1, j + step[1]))] not in island):
                checkIsland(
                    max(0, min(h - 1, i + step[0])), max(0, min(w - 1, j + step[1])))


for i in range(h):
    for j in range(w):
        if ([i, j] not in island):
            if (grid[i][j] == "1"):
                checkIsland(i, j)
                n += 1
print(n)
