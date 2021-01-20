maks = 0
nums = [1,5,4,5]
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j and (nums[i]-1) * (nums[j]-1) > maks:
            maks = (nums[i] - 1) * (nums[j] - 1)
print(maks)