nums = list(map(int, input().split()))
n = int(input())

newArray = []
x = True
xCount = 0
yCount = n
for i in range(2*n):
    if x:
        newArray.append(nums[xCount])
        xCount += 1
        x = False
    else:
        newArray.append(nums[yCount])
        yCount += 1
        x = True
print(newArray)