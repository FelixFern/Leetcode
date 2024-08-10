class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum([(i * (i % m != 0)) - (i * (i % m == 0)) for i in range(1, n + 1)])
