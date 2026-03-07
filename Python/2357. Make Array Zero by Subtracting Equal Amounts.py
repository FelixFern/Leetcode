class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = set(nums)
        
        return len(res) if 0 not in nums else len(res) - 1