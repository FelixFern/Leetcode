class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        stack = ""

        for i in command:
            stack += i
            if (stack == "G"):
                res += "G"
                stack = ""
            elif (stack == "()"):
                res += "o"
                stack = ""
            elif (stack == "(al)"):
                res += "al"
                stack = ""

        return res
