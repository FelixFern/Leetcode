class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        rows = len(mat)

        for i in range(rows):
            heappush(heap, (sum(mat[i]), i))

        res = []
        for i in range(k):
            res.append(heappop(heap)[1])

        return res
