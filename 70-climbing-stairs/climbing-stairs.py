class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def dfs(current, goal):
            if current == goal:
                return 1
            elif current > goal:
                return 0

            if current in memo:
                return memo[current]

            memo[current] = dfs(current + 1, goal) + dfs(current + 2, goal)
            return memo[current]

        return dfs(0, n)
        