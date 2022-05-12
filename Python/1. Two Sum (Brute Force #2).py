nums = [3,2,4]
target = 6
for i in range(len(nums)):
    x = target - nums[i]
    for j in range(len(nums)):
        if i == j:
            pass
        elif x == nums[j]:
            print(i,j)
            break 