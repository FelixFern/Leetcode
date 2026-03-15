class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = []
        heappush_max(heap, a)
        heappush_max(heap, b)
        heappush_max(heap, c)
        
        score = 0

        while sum(heap) > max(heap):
            first = heappop_max(heap)
            second = heappop_max(heap)
            score += 1

            heappush_max(heap, first - 1)
            heappush_max(heap, second - 1)

        return score
            