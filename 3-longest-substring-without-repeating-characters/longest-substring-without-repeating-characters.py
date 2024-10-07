class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        
        start = 0
        max_length = 0
        
        for end in range(len(s)):
            if s[end] in char_set:
                while s[end] in char_set:
                    char_set.remove(s[start])
                    start += 1
            
            char_set.add(s[end])
            
            current_length = end - start + 1
            if current_length > max_length:
                max_length = current_length
        
        return max_length