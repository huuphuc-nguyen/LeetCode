class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        stack = []
        
        for word in words:
            if len(word) > 0:
                stack.append(word)
        
        stack.reverse()
        return (" ").join(stack)

