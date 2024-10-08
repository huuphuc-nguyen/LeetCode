class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
    
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each string in the list
        for string in strs[1:]:
            # Reduce the prefix until it matches the beginning of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix