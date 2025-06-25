class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         # pw*wk*ew
        # max = 2
        if s is None or s == "": return 0

        left = right = 0
        max_lenght = 1
        window = []
        window.append(s[0])

        for i in range(1,len(s)):
            # check the next char to see if it is in the window or not
            if s[i] not in window:
                window.append(s[i])
                continue
            else:
                print(max_lenght)
            # update maxlenght
                if len(window) > max_lenght:
                    max_lenght = len(window)
            # narrow the window until the repeated character is not in the window anymore
                while len(window) != 0 and s[i] in window :
                    window.pop(0)
                window.append(s[i])
        print(window)
        return max(max_lenght, len(window))
