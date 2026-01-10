class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)  # Initialize a DP table with infinity for amounts 0 to 'amount'
        dp[0] = 0  # Base case: 0 coins needed to make an amount of 0
        # print("Initial DP table:", dp)
        for coin in coins:  # Iterate through each coin denomination
            for i in range(coin, amount + 1):  # Iterate through amounts from 'coin' to 'amount'
                dp[i] = min(dp[i], dp[i - coin] + 1)  # Update the minimum number of coins needed for amount 'i'
                # either keep the current value, or use the current coin and add 1 to the number of coins needed for the remaining amount

        return dp[amount] if dp[amount] != float('inf') else -1  # Return the minimum coins needed for 'amount', or -1 if it's impossible

                
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))  # Output: 3