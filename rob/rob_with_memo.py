class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dfs dp problem where you 
        #choose to rob or not to rob 
        #so either max(0+dp(next),nums[i])
        memo = {}
        def dfs(i): 
            if i >= len(nums): 
                return 0
            if i in memo: 
                return memo[i]
            memo[i] = max(nums[i] + dfs(i+2), 0+ dfs(i+1))
            return memo[i]

        return dfs(0)