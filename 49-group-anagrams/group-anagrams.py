import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hashMap = collections.defaultdict(list)
        ans = []

        for string in strs:
            sortedStr =  "".join(sorted(string)) 
            hashMap[sortedStr].append(string)

        return list(hashMap.values())