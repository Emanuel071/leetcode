class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # dp[i] will be the length of LIS ending at index i
        # print(dp)
        for i in range(1, n):
            print(f"i={i}, nums[i]={nums[i]}")
            # print(range(1, n))
            for j in range(i):
                print(f"  j={j}, nums[j]={nums[j]}")
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
    # print(sol.lengthOfLIS([0,1,0,3,2,3]))  # Output: 4
    # print(sol.lengthOfLIS([7,7,7,7,7,7,7]))  # Output: 1