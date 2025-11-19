class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # using dynamic programming
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(5)  # Output: 8
    print(result)

        