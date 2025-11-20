class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n
        print(output)

        # Calculate left products
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        print("Left products:")
        print(output)
        # Calculate right products and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        print("Final output with right products:")
        print(output)
        return output
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.productExceptSelf([1, 2, 3, 4])  # Output: [24, 12, 8, 6]
    print(result)

        