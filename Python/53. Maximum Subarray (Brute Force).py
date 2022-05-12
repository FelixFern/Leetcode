#WIP (TLE) 
import math
arr = [-2,1,-3,4,-1,2,1,-5,4]
maks = -math.inf
size = len(arr)
start = 0
end = size
while size != 0:
    sums = 0
    for i in range(start,end):
        sums += arr[i] 
    if maks <= sums:
        maks = sums
    if end == len(arr):
        size -= 1
        start = 0
        end = size
    else:
        start += 1
        end += 1
print(maks)
