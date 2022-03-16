stepsCache = {}

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in stepsCache:
            return stepsCache[n]
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            numOfWays = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        stepsCache[n] = numOfWays
        return numOfWays
        