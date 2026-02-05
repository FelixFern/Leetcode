class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = nums[:n], nums[n:]
        res = []

        for i in range(len(nums)):
            if(i % 2 == 0):
                res.append(left[i // 2])
            else: 
                res.append(right[i // 2])
        return res
