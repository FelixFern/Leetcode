#TLE https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
import math
arr = [17,18,5,4,6,1]
size = len(arr)
target = []
end = 0
for i in range(size):
    biggest = -math.inf
    for j in range(i+1, end):
        if arr[j] >= biggest:
            biggest == arr[j]
            end = j
        arr[j] = biggest
print(arr)
        