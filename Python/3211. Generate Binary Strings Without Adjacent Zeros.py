class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def dp(bits):
            if (len(bits) == n):
                res.append(bits)
                return

            if (bits[-1] == "0"):
                dp(bits + "1")
            else:
                dp(bits + "0")
                dp(bits + "1")

        dp("0")
        dp("1")
        return res
