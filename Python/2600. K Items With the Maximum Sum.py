class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0

        res += min([numOnes, k])
        k = (k - (numOnes + numZeros) >= 0) * (k - (numOnes + numZeros))
        res += min([numNegOnes, k]) * -1

        return res
