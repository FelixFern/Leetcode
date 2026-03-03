class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heappush(heap, -i)

        res = 0
        for i in range(k):
            res = heappop(heap)
            
        return -res