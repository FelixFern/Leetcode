class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        i = 1

        while i < n and nums[i] > nums[i - 1]:
            i += 1
        if i == 1:
            return False

        j = i
        while j < n and nums[j] < nums[j - 1]:
            j += 1
        if j == i:
            return False

        k = j
        while k < n and nums[k] > nums[k - 1]:
            k += 1
        if k == j:
            return False

        return k == n
