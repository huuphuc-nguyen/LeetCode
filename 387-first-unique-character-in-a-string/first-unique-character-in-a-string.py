import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        myMap = collections.defaultdict(int)
        for char in s:
            myMap[char] += 1
        
        
        for i in range(len(s)):
            if myMap[s[i]] == 1:
                return i
        return -1