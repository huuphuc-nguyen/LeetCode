class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:  # Collision condition
                if abs(asteroid) > abs(stack[-1]):  # Current asteroid is larger
                    stack.pop()
                elif abs(asteroid) == abs(stack[-1]):  # Both are the same size
                    stack.pop()
                    asteroid = 0  # Current asteroid also explodes
                    break
                else:  # Top asteroid is larger
                    asteroid = 0  # Current asteroid explodes
                    break
            
            if asteroid:  # If the asteroid is not destroyed, add it to the stack
                stack.append(asteroid)
        
        return stack