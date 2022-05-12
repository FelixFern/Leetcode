nums = [12,3,4,5,6,7]
target = int(input())
mid = int(len(nums)/2)
i, j = 0, len(nums)-1

if len(nums) > 1:
    while True:
        if nums[mid] > target:
            j = mid - 1
            mid = i + int((j - i) / 2)
        elif nums[mid] < target:
            i = mid + 1
            mid = i + int((j - i) / 2)
        if nums[mid] == target:
            print(mid)
            break
        if j - i <= 0:
            print(-1)
            break
else: 
    if nums[0] == target:
        print(target)
    else:
        print(-1)
