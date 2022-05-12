nums = [1,1,0,1,0,1,0,0,1,1,1,1]
count = 0
biggest = 0 
for i in nums:
    if i == 1:
        count +=1 
    else:
        count = 0
    if biggest < count:
        biggest = count
print(biggest)