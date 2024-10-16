class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []

        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        
        return len(stack) == 0
        