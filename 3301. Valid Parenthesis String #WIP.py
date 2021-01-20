s = "(**)))"
splitted = [str (i) for i in s]
size = len(splitted)
start = 0
end = 1

while True:
    if size == 0 :
        print("True")
        break
    if splitted[start] == "(":
        if splitted[end] == ")":
            del splitted[start]
            del splitted[end]
            end = 1
        else:
            end += 1
    elif splitted[start] == "*":
        if splitted[end] == ")":
            del splitted[start]
            del splitted[end]
            end = 1
        else: 
            end += 1
    elif splitted[end] == "*" and splitted[start] == "(":
        del splitted[start]
        del splitted[end]
        end = 1
    else:
        print("False")
        break
