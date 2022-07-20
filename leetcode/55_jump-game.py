class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        
        dp = [False] * len(nums)
        
        for i in range(nums[0] + 1):
            if i >= len(dp): break
            dp[i] = True
        
        for i in range(1, len(dp)):
            if not dp[i]: continue
            if dp[-1]: return True
                
            for j in range(1, nums[i] + 1):
                if i+j >= len(dp): break
                    
                if not dp[i+j]:
                    dp[i+j] = True
                    if dp[-1]: return True
        return False