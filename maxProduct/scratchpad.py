class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_prod = float('-inf')

        if len(nums) < 2:
            return nums[0]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = nums[i]*nums[j]
                # print(f"i: {i}, j: {j}, nums[i]: {nums[i]}, nums[j]: {nums[j]}, prod: {prod}")
                if prod > largest_prod and j - i == 1:
                    largest_prod = prod
                    # print(largest_prod)
            if largest_prod == float('-inf') or largest_prod == 0 or largest_prod < max(nums):
                largest_prod = max(nums)
                
        return largest_prod

class Solution(object):
    def maxProduct_again(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's Algorithm adaptation for maximum product subarray
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current * nums[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct_again([2,3,-2,4]))  # Output: 6
    print(sol.maxProduct_again([-2,0,-1]))  # Output: 0
    print(sol.maxProduct_again([-2,-3,4]))  # Output: 24
    print(sol.maxProduct_again([0,2]))  # Output: 2
    print(sol.maxProduct_again([-2]))  # Output: -2
    print(sol.maxProduct_again([-2,3,-4]))  # Output: 24

