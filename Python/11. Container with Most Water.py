class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1

        curr = (len(height) - 1) * min(height[lp], height[rp])
        curr_best = curr

        while lp != rp:
            val_1 = min(height[lp + 1], height[rp]) * (rp - lp - 1)
            val_2 = min(height[lp], height[rp - 1]) * (rp - lp - 1)
            if (height[lp] <= height[rp]):
                lp = lp + 1
                curr = val_1
            else:
                rp = rp - 1
                curr = val_2

            if (curr > curr_best):
                curr_best = curr

        return curr_best
