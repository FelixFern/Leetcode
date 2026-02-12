class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """

        if (not ops):
            return m * n

        min_row = float("inf")
        min_col = float("inf")

        for op in ops:
            min_row = min(op[0], min_row)
            min_col = min(op[1], min_col)

        return min_row * min_col
