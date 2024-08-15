class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        res = 0

        lp = 0
        rp = len(piles) - 1

        while lp < rp:
            res += piles[rp - 1]
            lp += 1
            rp -= 2
        return res
