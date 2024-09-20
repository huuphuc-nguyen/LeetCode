class Solution(object):

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 0
        elif n % 2 == 0:
            return self.integerReplacement(n/2) + 1
        else:
            plus_1 = self.integerReplacement(n+1)
            minus_1 = self.integerReplacement(n-1)
            
            result = min(plus_1, minus_1)
            
            return result + 1
        
