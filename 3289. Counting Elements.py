arr = [1,1,2,2,3]
count = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: 
            pass
        elif arr[i]+1 == arr[j]:
            count+=1
            break
print(count)