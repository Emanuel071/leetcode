class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(result, max_so_far)

        return result
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))  # Output: 6
    print(sol.maxProduct([-2,0,-1]))  # Output: 0
    print(sol.maxProduct([-2,-3,4]))  # Output: 24
    print(sol.maxProduct([0,2]))  # Output: 2
    print(sol.maxProduct([-2]))  # Output: -2
    print(sol.maxProduct([-2,3,-4]))  # Output: 24
