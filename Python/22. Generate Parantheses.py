class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        possible = []

        def generate(curr, o, c):
            if (o == n and c == n):
                possible.append(curr)

            if (o < n):
                generate(curr + "(", o + 1, c)
            if (c < n and o > c):
                generate(curr + ")", o, c + 1)

        generate("(", 1, 0)

        return possible
