class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # coinchange problem using dynamic programming and recursion with memoization
        memo = {}
        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            
            min_coins = float('inf')
            for coin in coins:
                res = dfs(remaining - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)
            memo[remaining] = min_coins
            return memo[remaining]
        result = dfs(amount)
        return result if result != float('inf') else -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))  # Output: 3