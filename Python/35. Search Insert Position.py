class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        temp = nums
        idx = 0
        while len(temp) > 1:
            index = len(temp) // 2
            if (temp[index] > target):
                temp = temp[:index]
            else:
                temp = temp[index:]
                idx += index
        if (temp[0] >= target):
            return idx

        return idx + 1
