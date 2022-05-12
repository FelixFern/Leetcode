num = 9669
splitted = [str (i) for i in str(num)]
re = ""
for i in range(len(splitted)):
    if splitted[i] == "6":
        splitted[i] = "9"
        break
for i in splitted:
    re += i
print(re)