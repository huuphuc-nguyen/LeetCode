class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        s = list(s)
        total_shifts = 0
        
        for i in range(len(shifts) - 1, -1, -1):
            total_shifts += shifts[i]
            s[i] = chr((ord(s[i]) - ord('a') + total_shifts) % 26 + ord('a'))
        
        return "".join(s)
