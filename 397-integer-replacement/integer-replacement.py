class Solution(object):

    memo = {}

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in self.memo:
            return self.memo[n]

        if (n == 1):
            return 0
        elif (n%2 == 0):
            result = 1 + self.integerReplacement(n/2)
        else:
            result = 1+  min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        
        self.memo[n] = result
        return result
        