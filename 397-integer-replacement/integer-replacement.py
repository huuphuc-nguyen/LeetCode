class Solution(object):

    memo = {}

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in self.memo:
            return self.memo[n]

        if n == 1:
            result = 0
            return 0
        elif n % 2 == 0:
            result = self.integerReplacement(n/2) + 1
            return result
        else:
            plus_1 = self.integerReplacement(n+1)
            minus_1 = self.integerReplacement(n-1)
            
            result = min(plus_1, minus_1)
    
            self.memo[n] = result + 1

            return result + 1
        
