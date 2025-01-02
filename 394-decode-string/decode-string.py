class Solution:
    def decodeString(self, s: str) -> str:

        # stack = []
        # result = ""
        # digit = 0
        # for char in s:
        #     if char.isdigit():
        #         if result != "":
        #             stack.append(result)
        #             result=""
        #         digit = digit*10 + int(char)
        #         continue
        #     if char == "[":
        #         stack.append(digit)
        #         digit = 0
        #         continue
        #     if char.isalpha():
        #         result += char
        #         continue
        #     if char == "]":
        #         popchar = stack.pop()
        #         if isinstance(popchar,int):
        #             temp =""
        #             for i in range(int(popchar)):
        #                 temp += result
        #             result = temp
        #             continue
        #         else:
        #             temp = popchar + result
        #             result = temp
        #             continue
        
        # while len(stack) != 0:
        #     popchar = stack.pop()
        #     if isinstance(popchar,int):
        #             temp =""
        #             for i in range(int(popchar)):
        #                 temp += result
        #             result = temp
        #             continue
        #     else:
        #         temp = popchar + result
        #         result = temp
        #         continue
        # return result

        stack = []
        current_string = ""
        current_number = 0

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == "[":
                stack.append((current_string, current_number))
                current_string = ""
                current_number = 0
            elif char == "]":
                prev_string, number = stack.pop()
                current_string = prev_string + current_string * number
            else:
                current_string += char

        return current_string


