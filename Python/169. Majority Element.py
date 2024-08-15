class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        calc = {}
        for i in nums:
            calc[i] = calc.get(i, 0) + 1

        return max(calc, key=calc.get)
