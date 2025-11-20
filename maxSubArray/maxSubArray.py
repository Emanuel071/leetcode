class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current = max_global = nums[0]
        # print(f"Initial max_current: {max_current}, max_global: {max_global}")  # Debug statement
        print(range(1, len(nums)))
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            # print(f"Index: {i}, Num: {nums[i]}, max_current: {max_current}")  # Debug statement
            if max_current > max_global:
                max_global = max_current
                # print(f"Updated max_global: {max_global}")  # Debug statement

        return max_global

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6