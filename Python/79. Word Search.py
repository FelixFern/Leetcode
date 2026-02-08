class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        word_size = len(word)

        def traverse(y, x, curr, size):
            if (size > word_size):
                return False

            if (curr == word):
                return True

            temp = board[y][x]
            board[y][x] = "#"

            for child in get_children(y, x):
                curr_char = board[child[0]][child[1]]
                if (curr_char == word[size]):
                    if (traverse(child[0], child[1], curr + curr_char, size + 1)):
                        return True

            board[y][x] = temp
            return False

        def get_children(y, x):
            steps = [
                [0, 1],
                [1, 0],
                [0, -1],
                [-1, 0]
            ]

            children = []

            for step in steps:
                x_step, y_step = x + step[0], y + step[1]

                if (0 <= x_step < m and 0 <= y_step < n and board[y_step][x_step] != "#"):
                    children.append([y_step, x_step])
            return children

        for y in range(n):
            for x in range(m):
                if (board[y][x] == word[0]):
                    if traverse(y, x, word[0], 1):
                        return True

        return False
