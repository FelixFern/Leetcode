class Solution:
    def scoreOfString(self, s: str) -> int:
        val = []
        res = 0
        for i in s: 
            val.append(ord(i))

        for i in range(len(val) - 1):
            res += abs(val[i] - val[i + 1])

        return res