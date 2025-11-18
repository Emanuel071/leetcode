class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            print(f"Current Number: {num}, Seen Set: {seen}")  # Debug statement
            if num in seen:
                return True
            seen.add(num)
        return False
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))  # Output: True
    print(sol.containsDuplicate([1,2,3,4]))  # Output: False
        