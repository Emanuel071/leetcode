# 1. Fibonacci - Basic DP (Memoization)
def fib_memo(n, memo={}):
    """
    Calculate nth Fibonacci number using memoization.
    Stores previously computed results to avoid redundant calculations.
    Time: O(n), Space: O(n)
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# 2. Coin Change - Bottom-Up DP
def coin_change(coins, amount):
    """
    Find minimum coins needed to make amount.
    Builds solution from bottom up using a table.
    Time: O(amount * len(coins)), Space: O(amount)
    """
    dp = [float('inf')] * (amount + 1)  # Initialize a DP table with infinity for amounts 0 to 'amount'
    dp[0] = 0  # Base case: 0 coins needed to make an amount of 0

    for coin in coins:  # Iterate through each coin denomination
        for i in range(coin, amount + 1):  # Iterate through amounts from 'coin' to 'amount'
            dp[i] = min(dp[i], dp[i - coin] + 1)  # Update the minimum number of coins needed for amount 'i'
            # either keep the current value, or use the current coin and add 1 to the number of coins needed for the remaining amount

    return dp[amount] if dp[amount] != float('inf') else -1  # Return the minimum coins needed for 'amount', or -1 if it's impossible


# 3. Longest Common Subsequence - 2D DP
def lcs(text1, text2):
    """
    Find length of longest common subsequence between two strings.
    Uses 2D table to track overlapping subproblems.
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


# 4. House Robber - 1D DP
def rob(nums):
    """
    Maximum sum of non-adjacent elements.
    Each state depends only on previous values.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    prev2, prev1 = 0, nums[0]
    
    for i in range(1, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    
    return prev1


# 5. Edit Distance - 2D DP
def editDistance(word1, word2):
    """
    Minimum operations to transform word1 to word2.
    Common operations: insert, delete, replace.
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]