class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found_zero = False

        for i in s:
            if (found_zero and i == "1"):
                return False
            if i == "0":
                found_zero = True

        return True
