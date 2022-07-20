# good dp solution
# dp[i]: i번째에서 가장 멀리갈 수 있는 index 번호
class Solution2(object):
    def canJump(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)-1):
            if dp[i-1] < i:
                return False
            
            dp[i] = max(dp[i-1], i+nums[i])
            
            if dp[i-2] >= len(nums)-1:
                return True
        
        return dp[len(nums)-2] >= len(nums)-1

# 첫 제출 (bad time complexity)
# 완전탐색
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