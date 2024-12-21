class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        maxCount = 0
        currentCount = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(k):
            if s[i] in vowels:
                currentCount +=1
        
        maxCount = currentCount

        for i in range(k, len(s)):
            if s[i] in vowels:
                currentCount+=1
            if s[i-k] in vowels:
                currentCount -=1
            
            maxCount = max(maxCount, currentCount)
        
        return maxCount

          