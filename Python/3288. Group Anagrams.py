strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sort = []
target = []
x = 1
y = 0
size = len(strs)
for i in strs:
    sort.append(''.join(sorted(i)))
def check(x,y,sort,target,size):
    if size == 0:
        pass
    else:
        target.append([])
        target[y].append(strs[0])
        i = 1
        while i < size:
            if sort[0] == sort[i]:
                target[y].append(strs[i])
                del sort[i]
                del strs[i]
                size -= 1
            else:
                i +=1
        del sort[0]
        del strs[0]
        size -=1
        y += 1
        check(x,y,sort,target,size)
check(x,y,sort,target,size)
print(target)