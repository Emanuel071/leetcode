class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # clean the string by removing non-alphanumeric characters and converting to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        # check if the cleaned string is equal to its reverse
        return cleaned == cleaned[::-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("racecar"))  # Output: True
    print(sol.isPalindrome("hello"))     # Output: False
    print(sol.isPalindrome("A man, a plan, a canal: Panama")) # Output: True