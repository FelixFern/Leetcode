class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_count = {}
        res = []

        for i in nums:
            num_count[i] = num_count.get(i, 0) + 1

        total_unique = len(num_count)

        while num_count:
            temp = []
            count = 0
            for i in num_count:
                if (num_count[i] > 0):
                    temp.append(i)
                    num_count[i] = num_count.get(i) - 1
                    count += 1

            if (count == 0):
                return res

            res.append(temp)
