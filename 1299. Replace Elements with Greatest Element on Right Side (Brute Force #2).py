#TLE https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
import math
arr = [17,18,5,4,6,1]
size = len(arr)
for i in range(size):
    biggest = -math.inf
    if i == size-1:
        arr[i] = -1
    else:
        for j in range(i+1, size):
            if arr[j] >= biggest:
                biggest = arr[j] 
        arr[i] = biggest
print(arr)