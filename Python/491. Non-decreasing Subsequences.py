class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dp(prev, lastIndex):
            if (lastIndex == len(nums)):
                return
            for i in range(lastIndex, len(nums)):
                temp = prev[:]
                if (temp[-1] <= nums[i]):
                    temp.append(nums[i])
                    if (temp not in res):
                        print(temp, i)
                        res.append(temp)
                    dp(temp, i + 1)

        for i, val in enumerate(nums):
            dp([val], i + 1)
        return res
