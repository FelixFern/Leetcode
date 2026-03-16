class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in stones:
            heappush_max(heap, i)


        while True:
            if(len(heap) <= 1):
                return heap[0] if len(heap) == 1 else 0

            first = heappop_max(heap)
            second = heappop_max(heap)
            delta = first - second

            if(delta > 0):
                heappush_max(heap, delta)