class Solution:
    def printVertically(self, s: str) -> List[str]:
        splitted = s.split(" ")
        max_len = max([len(i) for i in splitted])

        res = ["" for i in range(max_len)]

        for idx, i in enumerate(splitted):
            for j in range(max_len):
                if(j < len(i)):
                    print(i, j, idx, res)
                    res[j] += i[j]
                else: 
                    res[j] += " "
        return ([i.rstrip() for i in res])