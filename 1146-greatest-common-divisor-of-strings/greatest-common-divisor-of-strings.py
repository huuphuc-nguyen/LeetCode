class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        def isDivisor(str, divisor):
            # if (len(str) % len(divisor) != 0):
            #     return False
            
            # multiple_time = len(str) // len(divisor)

            # compare_string = ""
            # for i in range(multiple_time):
            #     compare_string += divisor
            #     if compare_string == str:
            #         return True
            
            # return False
            return str == divisor * (len(str) // len(divisor))

        if str1 + str2 != str2 + str1:
            return ""

        from math import gcd
        gcd_len = gcd(len(str1), len(str2))
        candidate = str1[:gcd_len]

        if isDivisor(str1, candidate) and isDivisor(str2, candidate):
            return candidate
        
        return ""
        
        # prefix = "" 
        # result = ""
        # min_len = len(str1) if len(str1) < len(str2) else len(str2)

        # for index in range(min_len):
        #     if str1[index] != str2[index]: return ""
        #     prefix += str1[index]

        #     if isDivisor(str1, prefix) and isDivisor(str2, prefix):
        #         result = prefix
        
        # return result