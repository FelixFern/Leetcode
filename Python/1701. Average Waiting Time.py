class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        lastFinishedTime = 0
        waitingTime = 0

        for idx, val in enumerate(customers): 
            if(idx == 0):
                lastFinishedTime = val[0] + val[1]
                waitingTime += val[1]
            else:
                lastFinishedTime = max(val[0], lastFinishedTime) + val[1]
                waitingTime += lastFinishedTime - val[0]

        return waitingTime / len(customers)