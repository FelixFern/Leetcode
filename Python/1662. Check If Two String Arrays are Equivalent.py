word1 = ["ab", "c"]
word2 = ["a", "bc"]

x = ""
y = ""
for i in word1: 
    x += i 

for i in word2:
    y += i

if x == y:
    print(True)
else: 
    print(False)