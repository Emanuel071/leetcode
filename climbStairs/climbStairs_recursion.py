class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # using recursion with memoization
        memo = {}
        def dfs(steps):
            if steps in memo:
                return memo[steps]
            if steps <= 1:
                return 1
            memo[steps] = dfs(steps - 1) + dfs(steps - 2)
            return memo[steps]
        return dfs(n)
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(2)  # Output: 8
    print(result)

        