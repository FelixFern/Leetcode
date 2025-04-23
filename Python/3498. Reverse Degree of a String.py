class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum([((26 - (ord(i) - 97)) * (idx + 1)) for idx, i in enumerate(s)])
