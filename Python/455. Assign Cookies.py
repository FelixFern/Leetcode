g = [1, 2]
s = [1, 2, 3]

content = 0
g = sorted(g)
s = sorted(s)
for i in g:
    pointer = 0
    while len(s) > 0 and pointer <= len(s) - 1:
        if (s[pointer] >= i):
            s.remove(s[pointer])
            content += 1
            break
        pointer += 1
print(content)
