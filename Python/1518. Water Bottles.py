class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def exchange(fullbottles, empty, total):
            if (fullbottles + empty < numExchange):
                return total + fullbottles
            return exchange(empty // numExchange, fullbottles + empty - empty // numExchange * numExchange, total + fullbottles)

        return exchange(numBottles, 0, 0)
