class Solution:
    def fillCups(self, amount: List[int]) -> int:
        if(sum(amount) == 0):
            return 0

        heap = []
        count = 0

        for i in amount:
            heappush_max(heap, i)

        while len(heap) > 0:
            if(len(heap) == 1):
                count += heappop_max(heap)
                break

            count += 1
            a, b = heappop_max(heap), heappop_max(heap)
            a -= 1
            b -= 1

            if(a > 0):
                heappush_max(heap, a)
            if(b > 0):
                heappush_max(heap, b)

        return count
