nums = [8,1,2,2,3]
lesser = []
for i in nums:
    total = 0
    for j in nums: 
        if i == j: 
            pass
        else:
            if i > j:
                total += 1
    lesser.append(total)
