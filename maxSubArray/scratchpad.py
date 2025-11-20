nums = [-2,1,-3,4,-1,2,1,-5]

current_sum = {}
max_sum = float('-inf')
temp_sum = 0

temp_sum_list = []

for i in range(len(nums)):
    print(f"Index {i}, Num: {nums[i]}")
    temp_sum += nums[i]
    temp_sum_list.append(temp_sum)
    current_sum[i] = temp_sum
    if temp_sum > max_sum:
        max_sum = temp_sum
    if temp_sum < 0:
        temp_sum = 0