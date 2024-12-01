class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                string+=word1[i]+word2[i]
        elif len(word1)<len(word2):
            for i in range(len(word1)):
                string+=word1[i]+word2[i]
            string+=word2[len(word1):]
        else:
            for i in range(len(word2)):
                string+=word1[i]+word2[i]
            string+=word1[len(word2):]
        return(string)