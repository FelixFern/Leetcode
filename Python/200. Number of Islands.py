grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
w = len(grid[0])
h = len(grid)
steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]
n = 0


def checkIsland(i, j):
    if grid[i][j] == "1":
        grid[i][j] = "0"
        for step in steps:
            if (grid[max(0, min(h - 1, i + step[0]))][max(0, min(w - 1, j + step[1]))] == "1"):
                checkIsland(
                    max(0, min(h - 1, i + step[0])), max(0, min(w - 1, j + step[1])))


for i in range(h):
    for j in range(w):
        if (grid[i][j] == "1"):
            checkIsland(i, j)
            n += 1
print(n)
