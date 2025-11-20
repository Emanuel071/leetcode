
memo = {}
def coinneeds(coins, amount):
    
    if amount == 0:
        return 0
    
    memo[steps] = dfs(steps - 1) + dfs(steps - 2)

    return coinneeds(coins, amount)
