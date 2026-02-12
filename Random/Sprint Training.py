
# Pat is an ordinary kid who works hard to be a great runner. As part of training, Pat must run sprints of different intervals on a straight trail. The trail has numbered markers that the coach uses as goals.
# Pat's coach provides a list of goals to reach in order.
# Each time Pat starts at, stops at, or passes a marker it is considered a visit. Determine the lowest numbered marker that is visited the most times during Pat's day of training.
# Example n =5
# sprints = [2, 4, 1, 3]
# if the number of markers on the trail, n= 5, and
# assigned sprints = [2, 4, 1, 3], Pat first sprints from
# position 2 → 4. The next sprint is from position 4 → 1, and then 1 → 3. A marker numbered position p is considered to be visited each time Pat either starts or ends a sprint there and each time it is passed while sprinting.

def sprintTraining(n, sprints):
    d = [0] * (n + 1)

    for i in range(len(sprints) - 1):
        x, y = min(sprints[i], sprints[i + 1]), max(sprints[i], sprints[i + 1])

        d[x] += 1
        d[y + 1] -= 1

    for i in range(1, len(d)):
        d[i] = d[i] + d[i - 1]

    return d[1:]


print(sprintTraining(5, [2, 4, 1, 3]))
