arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 9]
d = 2

num_el = 0
for i in arr1:
    nope = False
    for j in arr2:
        if abs(i - j) <= d:
            nope = True
            break

    if (not nope):
        num_el += 1

print(num_el)
