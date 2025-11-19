class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dfs(steps, indent=0):
            print(' ' * indent + f"dfs({steps})")  # Print the current call
            if steps in memo:
                print(' ' * (indent + 2) + f"Returning memo[{steps}] = {memo[steps]}")
                return memo[steps]
            if steps <= 1:
                print(' ' * (indent + 2) + "Base case: returning 1")
                return 1
            print(' ' * (indent + 2) + f"Calling dfs({steps - 1})")
            left = dfs(steps - 1, indent + 4)
            print(' ' * (indent + 2) + f"Calling dfs({steps - 2})")
            right = dfs(steps - 2, indent + 4)
            memo[steps] = left + right
            print(' ' * (indent + 2) + f"memo[{steps}] = {left} + {right} = {memo[steps]}")
            return memo[steps]
        return dfs(n)
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(5)  # Output: 8
    print(result)

        