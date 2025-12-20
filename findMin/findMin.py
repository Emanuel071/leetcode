class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # binary search to find the minimum in a rotated sorted array
        left, right = 0, len(nums) - 1
        print(f"Initial nums: {nums}")

        while left < right:
            mid = (left + right) // 2
            print(f"left: {left}, mid: {mid}, right: {right}, nums[mid]: {nums[mid]}, nums[right]: {nums[right]}")

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        print(f"Minimum found at index {left}, value: {nums[left]}")
        return nums[left]

if __name__ == "__main__":
    sol = Solution()
    min_value = sol.findMin([3, 4, 5, 1, 2])  # Output: 1
    print(min_value)