releaseTimes = [9,29,49,50]
keysPressed = "cbcd"

candidate = {}


for i, val in enumerate(releaseTimes):
    if i == 0:
        candidate[val] = [keysPressed[i]]
    else: 
        candidate[val - releaseTimes[i - 1]] = candidate.get(val - releaseTimes[i - 1], [])
        candidate[val - releaseTimes[i - 1]].append(keysPressed[i])


print(max(candidate[max(candidate)]))