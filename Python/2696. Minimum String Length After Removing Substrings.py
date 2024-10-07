class Solution:
    def minLength(self, s: str) -> int:
        def removeSubstring(s, l):
            if("AB" in s):
                return removeSubstring(s.replace("AB", ""), l)
            elif("CD" in s):
                return removeSubstring(s.replace("CD", ""), l)
            return min(l, len(s))

        return removeSubstring(s, len(s))
