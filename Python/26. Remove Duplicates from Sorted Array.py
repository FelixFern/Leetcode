class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = nums[0]
        unique = [nums[0]]
        k = 1
        for i in nums:
            if i != current:
                current = i
                unique.append(i)
                k += 1

        for i in range(k):
            nums[i] = unique[i]

        return k
