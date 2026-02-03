class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        p = [0] * (n + 1)
        lp = 0
        rp = 0
        size = 1
        sums = 0

        for i in range(1, n + 1):
            p[i] = arr[i - 1] + p[i - 1]

        while size <= n and lp < n + 1:
            if (rp == n):
                lp = 0
                size += 2
                rp = size - 1
            else:
                print(lp, rp)
                sums += p[rp + 1] - p[lp]
                lp += 1
                rp += 1

        return sums
