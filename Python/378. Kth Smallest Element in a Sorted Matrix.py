class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []

        for row in matrix:
            for i in row:
                heappush(min_heap, i)

        for i in range(k):
            curr = heappop(min_heap)

        return curr