class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        numDistinct = len(set(nums))
        totalLength = len(nums)

        res = 0
        for i in range(totalLength):
            st = set()
            for j in range(i, totalLength):
                st.add(nums[j])
                if (len(st) == numDistinct):
                    res += 1
        return res
