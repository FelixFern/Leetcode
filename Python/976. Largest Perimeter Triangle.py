class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def isValid(arr):
            return arr[0] + arr[1] > arr[2] and arr[1] + arr[2] > arr[0] and arr[0] + arr[2] > arr[1]

        sortedNums = sorted(nums)[::-1]

        for i in range(len(sortedNums) - 2):
            if (isValid(sortedNums[i:i+3])):
                return sum(sortedNums[i:i+3])

        return 0
