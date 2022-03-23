class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        n = len(cost)
        
        # special case
        if n == 1:
            return cost[0]
        elif n == 2:
            return min(cost[0], cost[1])
        
        # init
        dp = [0] * len(cost)
        
        # base case
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # bottom-up
        for i in range (2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        return min(dp[-2], dp[-1])
        