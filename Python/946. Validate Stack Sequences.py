
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        p = 0

        for i in pushed:
            stack.append(i)

            while stack and stack[-1] == popped[p]:
                p += 1
                stack.pop()

        return len(stack) == 0
