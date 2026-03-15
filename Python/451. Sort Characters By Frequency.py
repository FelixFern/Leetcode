class Solution:
    def frequencySort(self, s: str) -> str:
        max_heap = []
        res = ""

        count = Counter(s)

        for i in count:
            heappush_max(max_heap, (count[i], i))

        while len(max_heap) > 0:
            curr = heappop_max(max_heap)
            res += curr[1] * curr[0]

        return res