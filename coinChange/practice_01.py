class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}


        if amount == 0:
            return 0

        def fewestnumberofcoin(coin, coins, amount):
            memo[coins[coin]] = 
            return(coins[coin])


        for coin in range(len(coins)):
            print(coin)
            return fewestnumberofcoin(coin, coins, amount) + fewestnumberofcoin(coin + 1, coins , amount)


            
            
  
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))  # Output: 3