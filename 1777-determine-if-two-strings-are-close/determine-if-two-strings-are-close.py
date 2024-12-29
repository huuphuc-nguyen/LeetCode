class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # hashmap
        # operation1: dont limit how many time it is used -> same frequency for each character
        # operation2: swap the frequencies of 2 characters

        import collections
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for char in word1:
            map1[char] += 1
        for char in word2:
            map2[char] += 1

        if len(map1.keys()) != len(map2.keys()):
            return False
        
        # Check if both have the same set of characters
        if set(map1.keys()) != set(map2.keys()):
            return False

        # Check if the frequencies can be rearranged
        if sorted(map1.values()) != sorted(map2.values()):
            return False

        return True