class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freqs = Counter(nums)
    heap = []

    for num, freq in freqs.items():
        heappush(heap, (-freq, num))

    return [heappop(heap)[1] for i in range(k)]