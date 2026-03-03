class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        curr = "0"

        def generate(bits):
            return "".join(["0" if bits[i] == "1" else "1" for i in range(len(bits) - 1, -1, - 1)])

        for i in range(1, n + 1):
            curr = curr + "1" + generate(curr)
        return curr[k - 1]
