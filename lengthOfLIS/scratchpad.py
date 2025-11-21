# class Solution(object):
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

list_ex = [5,6,3,4,8,1,2]

temp_longest_list = []

final_longest_list = []

for i in range(len(list_ex)):
    for j in range(i, len(list_ex)):
        if list_ex[j] <= list_ex[i]:
            continue
        if list_ex[j] > list_ex[i]:
            temp_longest_list.append(list_ex[j])
            print(temp_longest_list)
            if len(temp_longest_list) > len(final_longest_list):
                final_longest_list = temp_longest_list
    temp_longest_list = []
print("Final Longest List:")
print(final_longest_list)
