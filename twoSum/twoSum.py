class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for index, num in enumerate(nums):
            print(f"Index: {index}, Num: {num}")  # Debug statement
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []  # In case there is no solution, though the problem guarantees one.
    
if __name__ == "__main__":
    # Example usage (only runs when executed directly):
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]