class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """


        current_num = 0
        sign = 1
        rs = 0
        stack = []
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "+":
                rs += sign*current_num
                current_num = 0
                sign = 1
            elif char == "-":
                rs += sign*current_num
                current_num=0
                sign=-1
            elif char == "(":
                stack.append(rs)
                stack.append(sign)
                rs = 0
                sign = 1
            elif char == ")":
                rs += sign*current_num
                sign = stack.pop()
                old_rs = stack.pop()
                rs = old_rs + sign*rs
                current_num = 0
        
        rs +=sign*current_num

        return rs








            