class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        visited = set()

        for i in range(n):
            low = i + 1
            high = n - 1
            curr = nums[i]
            if (curr in visited):
                continue
            visited.add(curr)
            subvisited = set()
            while (low < high):
                l = nums[low]
                r = nums[high]
                delta = curr + r + l
                if (delta > 0):
                    high -= 1
                elif (delta < 0):
                    low += 1
                else:
                    if (l not in subvisited):
                        res.append([curr, l, r])
                    subvisited.add(l)
                    low += 1
        return res
