class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # init
        n = len(nums)
        
        # special case
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        # base cases
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # bottom-up
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]