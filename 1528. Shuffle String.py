s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
new = ""

for i in range(len(indices)):
    new += s[indices.index(i)]

print(new)