class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted = s.split(" ")

        p = len(splitted) - 1

        while splitted[p] == "":
            p -= 1
        return len(splitted[p])
