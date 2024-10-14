class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if(len(s) == 0):
            return True

        stack = []

        for i in s:
            if(len(stack) > 0):
                if i == ")" and stack[len(stack) - 1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return len(stack) 