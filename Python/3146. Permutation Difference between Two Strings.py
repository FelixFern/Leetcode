class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        for idx, val in enumerate(s):
            res += abs(idx - t.index(val))
        return res
