class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        seen = set()

        heappush(heap, 1)
        seen.add(1)

        for i in range(n):
            curr = heappop(heap)
            for j in [2, 3, 5]:
                new = curr * j
                if(new not in seen):
                    heappush(heap, new)
                    seen.add(new)
                    
        return curr