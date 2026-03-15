class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        max_heap = []
        count = Counter(words)

        for i in count:
            heappush(max_heap, (-count[i], i))
        
        res = []
        for i in range(k):
            res.append(heappop(max_heap)[1])
        
        return res
