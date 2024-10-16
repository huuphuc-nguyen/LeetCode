class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """


        # 1 - ( -2)
        #   c

        # number = 1
        # sum = 1
        # sign = -1

        # stack <- sum <- sign

        # sum += sign*number

        # old_sign = stack.pop()
        # sum = sum * old_sign




        # number = 0
        # sign = 1




        number = 0
        sign = 1
        sum = 0
        stack = []

        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == "+":
                sum += sign*number
                number = 0
                sign = 1
            elif c == "-":
                sum += sign*number
                number = 0
                sign = -1
            elif c == "(":
                stack.append(sum)
                stack.append(sign)
                sum = 0
                number = 0
                sign = 1
            elif c == ")":
                sum += sign*number

                old_sign = stack.pop()
                sum *= old_sign

                old_sum = stack.pop()
                sum+= old_sum

                number = 0
                sign = 1

            
        sum += sign*number

        return sum
        










            