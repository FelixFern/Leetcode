class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * (n + 1)

        for i in range(1, n + 1):
            ps[i] = nums[i - 1] + ps[i - 1]

        for i in range(n):
            left = ps[i + 1] - ps[0]
            right = ps[n] - ps[i]

            if (left == right):
                return i

        return -1
