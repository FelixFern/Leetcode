nums = [0,1,0,3,12]
x = 0
zeroCount = 0
for i in nums:
    if i == 0:
        zeroCount +=1
while zeroCount != 0:
    if nums[x] == 0:
        del nums[x]
        nums.append(0)
        zeroCount -= 1
    elif nums[x] != 0:
        x+=1
print(nums)