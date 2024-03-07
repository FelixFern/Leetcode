def canJump(nums):
    possible = [[0 for i in nums] for i in nums]

    for i, val in enumerate(nums):
        for j in range(val):
            if (i + j + 1 < len(nums)):
                possible[i][i + j + 1] = 1

    def find(to, adj):
        if (to == 0):
            return True

        can_from = [i for i in range(len(adj)) if adj[i][to] == 1]

        if len(can_from) == 0:
            return False

        return any(find(i, adj) for i in can_from)

    return find(len(nums) - 1, possible)


print(canJump([2, 3, 1, 1, 4]))
