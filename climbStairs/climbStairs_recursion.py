class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # using recursion with memoization
        # initialize memoization dictionary to cache computed results
        memo = {}

        # helper recursive function that returns number of ways for `steps`
        def dfs(steps):
            # return cached value if already computed
            if steps in memo:
                return memo[steps]
            # base case: 0 or 1 step -> exactly 1 way
            if steps <= 1:
                return 1
            # compute number of ways by summing ways for (steps-1) and (steps-2),
            # store result in memo to avoid recomputation
            memo[steps] = dfs(steps - 1) + dfs(steps - 2)
            # return the cached result
            return memo[steps]

        # start recursion for n steps
        return dfs(n)
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(2)  # Output: 8
    print(result)

        