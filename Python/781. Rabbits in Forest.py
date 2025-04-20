class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        count = {}
        for val in answers:
            count[val] = count.get(val, 0) + 1

        for i in count:
            if (i == 0):
                res += count[i]
            else:
                res += ceil(count[i] / (i + 1)) * (i + 1)

        return res
