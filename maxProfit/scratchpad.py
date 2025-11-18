prices = [7,1,5,3,6,4]
maximum = 0
minimum = 0

buy = 0

for i in range(len(prices)):
    print(f"Day {i}: Price = {prices[i]} Length: {len(prices)}")
    maximum = max(prices)
    maximum = min(prices)
    print(max(prices))
    print(min(prices))
    prices.pop(0)
    if prices[i] <= minimum:
        buy = prices[i]
        print(" Buy at:", buy)
    if prices[i] >= maximum:
        sell = maximum - buy
        print(" Sell at:", sell)

print(sell)    

