class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []

        for i in range(len(nums)):
            heappush(min_heap, [nums[i], i])

        for i in range(k):
            curr = heappop(min_heap)
            curr[0] *= multiplier
            heappush(min_heap, curr)

        while(len(min_heap) > 0):
            val, idx = heappop(min_heap)
            nums[idx] = val

        return nums