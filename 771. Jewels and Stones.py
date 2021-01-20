J = "aA"
S = "aAAbbbb"
jewel = [str(i) for i in str(J)]
stone = [str(i) for i in str(S)]
total = 0
for i in stone:
    for j in jewel:
        if i == j:
            total += 1
print(total)