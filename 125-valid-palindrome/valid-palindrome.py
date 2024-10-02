class Solution(object):
    def remove_character_at_index(s, index):
        return s[:index] + s[index + 1:]
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # edge cases
        if not s:
            return False
        if s.isspace():
            return True

        # pre-process string: remove space and non-alphanumeric characters
        # lowercase
        s2 = ''
        for char in s.lower(): 
            if char.isalnum():
                s2+=char


        # check for palindrome
        left = 0
        right = len(s2) - 1

        while left <= right:
            if(s2[left] != s2[right]):
                return False
            left +=1
            right -= 1

        return True