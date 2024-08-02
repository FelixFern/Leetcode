class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0

        for i in nums: 
            res += i % 3 != 0

        return res
        