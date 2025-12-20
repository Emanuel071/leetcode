# list_array = [3, 4, 5, 1, 2]

# temp_value = None

# for i in range(len(list_array)):
#     # print(f"Index {i}, Value: {list_array[i]}")
#     if temp_value is None or list_array[i] < temp_value:
#         temp_value = list_array[i] 

# print(f"Minimum value found: {temp_value}")


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_value = None
        for i in range(len(nums)):
            print(f"Index {i}, Value: {nums[i]}")
            if temp_value is None or nums[i] < temp_value:
                temp_value = nums[i] 
        
        return temp_value

if __name__ == "__main__":
    sol = Solution()
    min_value = sol.findMin([3, 4, 5, 1, 2])  # Output: 1
    print(min_value)