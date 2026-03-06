class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        heap = []

        for i in nums:
            heappush(heap, i)

        while len(heap) > 0:
            alice = heappop(heap)
            bob = heappop(heap)

            arr.append(bob)
            arr.append(alice)

        return arr
