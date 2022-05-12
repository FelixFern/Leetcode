nums = [0,1,2,3,4]
index = [0,1,2,2,1]
target = []
x = 0
for i in index:
    target.insert(i, nums[x])
    x += 1
print(target)