n = 2
ans = [0 for i in range(n + 1)]

for i in range(n + 1):
    for j in bin(i)[2:]:
        if j == "1":
            ans[i] += 1
print(ans)
