class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        currColor = image[sr][sc]
        m, n = len(image), len(image[0])
        visited = set()

        def flood(x, y):
            if (x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited):
                return

            visited.add((x, y))
            if (image[x][y] == currColor):
                image[x][y] = color
                flood(x + 1, y)
                flood(x - 1, y)
                flood(x, y + 1)
                flood(x, y - 1)

        flood(sr, sc)

        return image
