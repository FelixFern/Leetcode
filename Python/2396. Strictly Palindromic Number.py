class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def toBase(n, base):
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = ""
            num = n

            while num > 0:
                res = digits[num % base] + res
                num //= base
            return res

        for i in range(2, n - 1):
            baseN = toBase(n, i)
            if (baseN != baseN[::-1]):
                return False
        return True
