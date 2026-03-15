class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []

        for i in arr:
            heappush(min_heap, (abs(i - x), i))

        res = []

        for i in range(k):
            curr = heappop(min_heap)
            res.append(curr)
        
        return sorted([i[1] for i in res])