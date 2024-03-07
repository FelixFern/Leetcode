
def even(s, i, longest):
    temp_longest = longest
    if i == 0:
        return s[0]

    lp = i - 1
    rp = i + 1
    print(i)
    while True:
        print(lp, rp)
        if(lp == -1 or rp == len(s)):
            break
        if s[lp] == s[rp]:
            if len(temp_longest) < rp - lp + 1:
                temp_longest = s[lp:rp + 1]
            lp -= 1
            rp += 1
        else: 
            break

    return temp_longest

def odd(s, i, longest):
    temp_longest = longest

    lp = i
    rp = i + 1

    while True:
        if(lp == -1 or rp == len(s)):
            break
        if s[lp] == s[rp]:
            if len(temp_longest) < rp - lp + 1:
                temp_longest = s[lp:rp + 1]
            lp -= 1
            rp += 1
        else: 
            break

    return temp_longest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        for i in range(len(s) * 2):
            if(i % 2 == 0):
                longest = odd(s, (i - 1) // 2 , longest)
            else: 
                longest = even(s, i // 2, longest)

        return longest
