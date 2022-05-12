n = 4
start = 3

for i in range(start+2, n*2 + start, 2):
    start ^= i

print(start)