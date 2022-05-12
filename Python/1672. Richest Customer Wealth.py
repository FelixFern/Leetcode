accounts = [[1,5],[7,3],[3,5]]
maks = 0 

for i in range(len(accounts)):
    sums = 0
    for j in accounts[i]:
        sums += j 
    if sums >= maks:
        maks = sums

print(maks)
