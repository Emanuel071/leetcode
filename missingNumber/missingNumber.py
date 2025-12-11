class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

if __name__ == "__main__":
    sol = Solution()
    # Example usage:
    nums = [3, 0, 1]
    missing = sol.missingNumber(nums)
    print("Missing number is:", missing)  # Output: 2