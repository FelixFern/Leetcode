class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []

        for i in range(len(score)):
            heappush_max(heap, (score[i], i))

        for i in range(len(heap)):
            curr = heappop_max(heap)

            if(i == 0):
                score[curr[1]] = "Gold Medal" 
            elif(i == 1):
                score[curr[1]] = "Silver Medal" 
            elif(i == 2):
                score[curr[1]] = "Bronze Medal" 
            else:
                score[curr[1]] = str(i + 1)

        return score