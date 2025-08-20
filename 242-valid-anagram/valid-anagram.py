from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 dictionaries
        #  anagram

        #  dict1 = {
        #     'a': 3
        #     n: 1
        #     g 1 
        #     r 1 
        #     m 1
        #  }

        #  nagaram

        #  dict2 = {
        #     n 1
        #     a 3
        #     ...
        #  }
        # match thoes dicts if they match => true
        print
        return Counter(s) == Counter(t)