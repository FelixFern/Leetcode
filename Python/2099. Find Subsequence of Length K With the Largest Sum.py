class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for idx, val in enumerate(nums):
            heappush(heap, (val, idx))
            if(len(heap) > k):
                heappop(heap)

        heap.sort(key=lambda x: x[1])

        return [i for i, _ in heap]