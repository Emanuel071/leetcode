class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # coinchange problem using dynamic programming and not with recursion with memoization
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for remaining in range(1, amount + 1):
            for coin in coins:
                if remaining - coin >= 0:
                    dp[remaining] = min(dp[remaining], dp[remaining - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))  # Output: 3