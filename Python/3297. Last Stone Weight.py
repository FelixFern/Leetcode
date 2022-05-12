stones = [2,7,4,1,8,1]
maks = []
size = len(stones)
while size > 0:
    if size <= 1 and len(maks) == 0:
        break
    maks.append(max(stones))
    del stones[stones.index(max(stones))]
    size -= 1
    if len(maks) == 2:
        stones.append(abs(maks[0]-maks[1]))
        maks = []
        size += 1
print(stones)
