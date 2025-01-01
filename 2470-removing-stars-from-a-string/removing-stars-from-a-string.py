class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
                continue
            else:
                stack.append(char)
        
        result = ''.join(stack)
        return result

        