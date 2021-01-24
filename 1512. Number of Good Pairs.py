nums = [1,2,3,1,1,3]
count = 0 

for i in range(len(nums) - 1):
    for j in range(i, len(nums)):
        if nums[i] == nums[j] and i < j:
            count += 1
print(count)