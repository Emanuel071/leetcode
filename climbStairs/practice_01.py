class Solution(object):
    def climbStairs(self, n):
        
        # self.paths = 0
        # self.memo = {}
        # def steps(n, memo,paths):
        #     if n == 0:
        #         self.paths += 1
        #         self.memo[steps] = self.paths
        #         return self.paths
        #     if n < 0:
        #         return None
        #     if n > 0:
        #         steps(n - 1, self.paths), steps(n - 2, self.paths)
        # steps(n, self.paths)

        # return self.paths
        # using recursion with memoization
        memo = {}
        def dfs(steps):
            if steps in memo:
                return memo[steps]
            if steps <= 1:
                return 1
            memo[steps] = dfs(steps - 1) + dfs(steps - 2)
            print(memo)
            return memo[steps]
        return dfs(n)
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(4))  