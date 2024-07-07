class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1]
        ]

        kc = [[king[0], king[1]] for i in range(8)]
        done = [False for i in range(8)]

        while not all(done):
            for i, val in enumerate(done):
                if (not val):
                    kc[i][0] += directions[i][0]
                    kc[i][1] += directions[i][1]

                if (kc[i][0] < 0 or kc[i][0] >= 8 or kc[i][1] < 0 or kc[i][1] >= 8):
                    done[i] = True

                if (kc[i] in queens and kc[i] not in res):
                    res.append(kc[i])
                    done[i] = True
        return res
