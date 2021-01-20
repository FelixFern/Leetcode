nums = [3,2,4]
target = 6
for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            pass
        elif nums[i] + nums[j] == target:
            print(i,j)
            break