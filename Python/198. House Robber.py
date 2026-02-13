class Solution(object):
    def rob(self, nums):
        self.memo = {}
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not nums):
            return 0

        def robbing(idx):
            if (idx < 0):
                return 0

            if idx in self.memo:
                return self.memo[idx]

            res = max(robbing(idx - 2) + nums[idx], robbing(idx - 1))

            self.memo[idx] = res
            return res

        return robbing(len(nums) - 1)
