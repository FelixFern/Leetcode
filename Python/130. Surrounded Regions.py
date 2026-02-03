class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return
            if board[x][y] != "O":
                return

            board[x][y] = "#"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)

        for i in range(n):
            for j in range(m):
                if (board[i][j] == "#"):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
