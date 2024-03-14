class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        rp = 0
        longest = 1
        valid = True

        if (len(s) <= 1):
            return len(s)

        characters = {s[0]: 1}

        while True:
            if (rp - lp + 1 > longest and valid):
                longest = rp - lp + 1
            if (lp == rp and lp == len(s) - 1):
                break

            if (characters.get(s[rp], 0) == 0 and rp != len(s) - 1):
                rp += 1
                characters[s[rp]] = characters.get(s[rp], 0) + 1
                if (characters.get(s[rp], 0) > 1):
                    valid = False
                else:
                    valid = True
            elif ((characters.get(s[rp], 0) > 1 and rp != lp) or rp == len(s) - 1):
                characters[s[lp]] = characters.get(s[lp], 0) - 1
                lp += 1
            else:
                rp += 1
                characters[s[rp]] = characters.get(s[rp], 0) + 1
                if (characters.get(s[rp], 0) > 1):
                    valid = False
                else:
                    valid = True

        return longest
