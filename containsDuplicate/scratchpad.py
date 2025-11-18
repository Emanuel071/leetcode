class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        distinct = False
        sorted_sublist = sorted(nums)

        for i in range(len(sorted_sublist)):
            # print(sorted_sublist)
            if nums[i] in nums[i + 1:]:
                distinct = True
                break

        return distinct

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))  # Output: True
    print(sol.containsDuplicate([1,2,3,4]))  # Output: False