class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        maxGroupSize = max(groupSizes)
        group = [[] for i in range(maxGroupSize)]
        res = []

        for idx, val in enumerate(groupSizes):
            group[val - 1].append(idx)

        for idx, val in enumerate(group):
            count = 0

            if(val != []):
                res.append([])

            for i in val:
                if(count - 1 == idx):
                    count = 0
                    res.append([])
                res[-1].append(i)
                count += 1

        return res