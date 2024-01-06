nums = ["0"]
base10 = [int(i, 2) for i in nums]
max_base10 = int("".join(["1" for i in range(len(nums[0]))]), 2)

for i in range(max_base10 + 1):
    if i not in base10:
        base2 = bin(i)[2:]
        print("".join(["0" for i in range(len(nums[0]) - len(base2))]) + base2)
        break
