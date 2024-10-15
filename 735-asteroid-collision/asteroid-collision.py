class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        # 5 10 -5

        # stack = 5 10 10

        # collision when the upcoming value has opposite sign with the top value of stack:
        #     => if upcoming asteroid is smaller than the top then skip it
        #     => if up coming asteroid is bigget than the top, ex: 5 and up coming -10 => need a while loop to pop all the asteroid that less than upcoming value, then add it to stsack

        stack = []

        for asteroid in asteroids:
            destroyed = False

            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()  # Right-moving asteroid is smaller, it explodes
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()  # Both asteroids are the same size, both explode
                    destroyed = True
                    break
                else:
                    destroyed = True  # Current asteroid explodes, stack asteroid survives
                    break

            if not destroyed:
                stack.append(asteroid)
        
        return stack
        