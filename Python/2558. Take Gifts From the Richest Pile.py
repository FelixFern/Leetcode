class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for i in gifts:
            heappush_max(heap, i)

        for i in range(k):
            curr = floor(heappop_max(heap) ** 0.5)
            heappush_max(heap, curr)

        return sum(heap)
