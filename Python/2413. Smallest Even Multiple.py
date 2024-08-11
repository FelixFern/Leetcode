class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(a, b):
            if (b == 0):
                return a
            return gcd(b, a % b)

        return 2 * n // gcd(2, n)
