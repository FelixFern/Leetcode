s = "RLLLLRRRLR"
splitted = [str(i) for i in str(s)]
count = 0
RCount = 0
LCount = 0
for i in splitted:
    if i == "R":
        RCount += 1
    elif i == "L":
        LCount += 1
    if RCount == LCount:
        count += 1
        RCount, LCount = 0,0 
print(count)