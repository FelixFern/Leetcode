class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        invert = [-i for i in nums]
        heapify(invert)

        for _ in range(k):
            max_val = -heappop(invert)

            score += max_val 

            heappush(invert, -ceil(max_val / 3)) 

        return score