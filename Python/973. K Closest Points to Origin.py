class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculateDistSquared(x,y):
            return x ** 2 + y ** 2

        return sorted(points, key=lambda i: calculateDistSquared(i[0], i[1]))[:k]