class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        counter = {}
        res = []

        def binarySearch(arr, val):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = l + (r - l) // 2
                if (arr[m] == val):
                    return m
                elif (arr[m] > val):
                    r = m - 1
                else:
                    l = m + 1

            return -1

        for idx, val in enumerate(nums):
            if (counter.get(val) == None):
                counter[val] = [idx]
            else:
                counter[val].append(idx)

        for q in queries:
            num = nums[q]
            if (len(counter.get(num)) <= 1):
                res.append(-1)
            else:
                temp = counter.get(num)
                idx = binarySearch(temp, q)

                left = temp[idx - 1]
                right = temp[idx + 1] if idx + 1 < len(temp) else temp[0]
                minDist = inf

                leftDist = abs(q - left)
                rightDist = abs(q - right)

                leftDist = min(leftDist, len(nums) - leftDist)
                rightDist = min(rightDist, len(nums) - rightDist)
                minDist = min(leftDist, rightDist)

                res.append(minDist)

        return res
