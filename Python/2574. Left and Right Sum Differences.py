class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []

        sums = sum(nums)

        for idx, val in enumerate(nums):
            if idx == 0:
                leftSum.append(0)
            else:
                leftSum.append(nums[idx - 1] + leftSum[idx - 1])

        for val in nums:
            sums -= val
            rightSum.append(sums)

        return [abs(leftSum[i] - rightSum[i]) for i in range(len(nums))]
