S = "a#c"
T = "b"

def hashtag(data):
    splitted = [str(i) for i in data]
    key = 0
    size = len(splitted)
    while key != size:
        if splitted[key] == "#":
            if key == 0:
                del splitted[key]
                size -= 1
            else:
                del splitted[key]
                del splitted[key - 1]
                size -= 2
                key -= 1
        else:
            key += 1
    return splitted
if hashtag(S) == hashtag(T):
    print("TRUE")
else:
    print("FALSE")
            
