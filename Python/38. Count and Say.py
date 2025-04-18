class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        newRes = ""

        current, count = "", 0

        for i in range(n - 1):
            for idx, j in enumerate(res):
                if (idx == 0):
                    current, count = j, 1
                else:
                    if (current == j):
                        count += 1
                    else:
                        newRes += str(count) + str(current)
                        current, count = j, 1
            if (count > 0):
                res = str(newRes) + str(count) + str(current)

            current, count = "", 0
            newRes = ""

        return res
