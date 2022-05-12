import math
nums = [12,345,2,6,7896]
count = 0 
for i in nums:
    if int(math.log10(i) + 1) % 2 == 0:
        count += 1
print(count)