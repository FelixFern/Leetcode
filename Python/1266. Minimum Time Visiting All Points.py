points = [[3,2],[-2,2]]
time = 0
x = 0
y = 0
for i in range(len(points)-1):
    x = abs(points[i][0] - points[i+1][0])
    y = abs(points[i][1] - points[i+1][1])
    if x == y:
        time += x
    elif x != y:
        if x > y:
            time += x-y
            time += y
        else:
            time += y-x
            time += x
print(time)