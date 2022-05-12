arr = [-4,-1,0,3,10]
squared = []
def insertionSort(data):
    size = len(data)
    key = 1
    start = 1
    while start < size:
        if start == 0:
            start = key
        if abs(data[start]) < abs(data[start-1]):
            data[start],data[start-1] = abs(data[start-1]), abs(data[start])
            key = start
            start -= 1
        else: 
            start += 1
insertionSort(arr)
for i in arr:
    squared.append(i**2)
print(squared)