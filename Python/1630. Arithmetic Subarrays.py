class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """

        res = [False for i in range(len(l))]

        for i in range(len(l)):
            print(i)
            temp = sorted(nums[l[i]:r[i] + 1])
            stop = False
            if(len(temp) > 2):        
                delta = temp[0] - temp[1]
                for j in range(1, len(temp) - 1):
                    if(delta != temp[j] - temp[j + 1]):
                        stop = True
                        break
                if(not stop):
                    res[i] = True
            else:
                res[i] = True

        return res