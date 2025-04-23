class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            count[sum(map(int, str(i)))] += 1

        maxVal = max(count)

        res = 0
        for i in count:
            if i == maxVal:
                res += 1

        return res
