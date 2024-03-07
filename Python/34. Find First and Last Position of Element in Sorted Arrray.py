class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        right = nums[len(nums) // 2:]
        left = nums[:len(nums) // 2]
        r_s = len(left)
        l_s = 0

        l_t = None
        r_t = None

        if (len(nums) == 1):
            if (nums[0] == target):
                return [0, 0]
            else:
                return [-1, -1]

        while left != [] and right != []:
            if (len(left) == 1 and left[0] == target):
                l_t = l_s
            if (len(right) == 1 and right[0] == target):
                r_t = r_s

            if (max(left) >= target):
                left, right = left[:len(left) // 2], left[len(left) // 2:],
                l_s, r_s = l_s, l_s + len(left)
            else:
                left, right = right[:len(right) // 2], right[len(right) // 2:],
                l_s, r_s = r_s, r_s + len(left)

        if (l_t == None and r_t == None):
            return [-1, -1]
        else:
            if (l_t == None):
                l_t = r_t
            elif (r_t == None):
                r_t = l_t
            print(l_t, r_t)
            while True:
                if (l_t - 1 > 0 and nums[l_t - 1] == target):
                    l_t -= 1
                elif (r_t + 1 < len(nums) and nums[r_t + 1] == target):
                    r_t += 1
                else:
                    break
            return [l_t, r_t]
