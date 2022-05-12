candies = [2,3,5,1,3]
extraCandies = 3 
output = []

maks = max(candies)
for i in candies:
    if i + extraCandies >= maks:
        output.append(True)
    else:
        output.append(False)
print(output)