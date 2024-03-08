class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i, val in enumerate(s): 
            if i == 0 or len(stack) == 0:
                stack.append(val)
            else: 
                if(val == "]" and stack[len(stack) - 1] == "["):
                    stack.pop()
                elif(val == ")" and stack[len(stack) - 1] == "("):
                    stack.pop()
                elif(val == "}" and stack[len(stack) - 1] == "{"):
                    stack.pop()
                else: 
                    stack.append(val)
        
        return len(stack) == 0