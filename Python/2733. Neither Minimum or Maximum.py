nums = [3, 2, 1, 4]

if (len(nums) <= 2):
    print(-1)
else:
    for i in nums:
        if i != max(nums) and i != min(nums):
            print(i)
            break
