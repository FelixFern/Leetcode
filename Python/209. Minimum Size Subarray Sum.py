class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        p = [0] * (n + 1)

        for i in range(1, n + 1):
            p[i] = p[i - 1] + nums[i - 1]

        minLength = float("inf")

        lp = 0
        rp = 0

        while lp != n:
            currSum = p[rp + 1] - p[lp]
            if (currSum >= target):
                minLength = min(minLength, rp - lp + 1)
                lp += 1
            elif (rp == n - 1):
                lp += 1
            else:
                rp += 1

        if (minLength == float("inf")):
            return 0

        return minLength
