nums = [-2,1]
DPBest = nums[0]
newBest = nums[0]
for i in range(1, len(nums)):
    if nums[i] + DPBest >= nums[i]:
        DPBest = nums[i] + DPBest
    else: 
        DPBest = nums[i] 
    if DPBest >= newBest:
        newBest = DPBest   
print(newBest)