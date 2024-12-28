class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        # altitude:
        #  0 x1 x2 x3 x4 x5
        # gain
        #    -5 1  5  0 -7

        #    gain[0] = a[1] - a[0]
        #    => a[1] = gain[0] + a[0] = -5

        a = [0]


        for i in range(len(gain)):
            a.append(gain[i] + a[i])

        print(a)

        return max(a)
