nums = [1,1,2,3]
size = int(len(nums)/2)
data = []
for i in range(0,size):
    freq = nums[2*i]
    vel = nums[2*i+1]
    for j in range(freq):
        data.append(vel)
print(data)