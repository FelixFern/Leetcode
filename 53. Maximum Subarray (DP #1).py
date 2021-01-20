array = [1,-2,3,-4,-5]
best = [array[0]]
newBest = array[0]
maks = array[0]

for i in range(1, len(array)):
    if newBest + best[i-1] > newBest:
        newBest += array[i] 
        best.append(newBest)
    else:
        newBest = array[i]
        best.append(newBest)
for i in range(1, len(best)):
    if maks <= best[i]:
        maks = best[i]
print(maks)

