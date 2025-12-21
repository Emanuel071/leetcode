nums = [1,2,3,1]

length = len(nums)

dp = [0] * length

maxtemp = 0
sumtotal = 0

for i in range(length):
    for j in range(i):
        print("i: ", i, "j: ", j)
        if i - j >= 2:
            dp[i] = max(dp[i], dp[j] + nums[i])
            print("dp[i]: ", dp[i])

print(maxtemp)