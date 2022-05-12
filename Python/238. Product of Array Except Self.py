nums = [1,2,3,4]
left = [1]
right = []
output = []
length = len(nums)

#Left
for i in range(length-1):
    left.append(nums[i] * left[i])
#Rigth
for i in range(length):
    if length-i-1 == length - 1:
        right.append(1)
    else:
        right.append(nums[length-i]*right[i-1])

right.reverse()

for i in range(length):
    output.append(left[i] * right[i])
print(output)