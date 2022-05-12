s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]
splitted = [str (i) for i in s]
for i in shift:
    if i[0] == 0:
        splitted = splitted[i[1]:] + splitted[:i[1]]
    else: 
        splitted = splitted[-i[1]:] + splitted[:-i[1]]
print(splitted)
s = ''.join(splitted)
print(s)