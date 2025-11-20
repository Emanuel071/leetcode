class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # remove anything in the string that is not alphanumeric and make it lowercase
        s = ''.join(char.lower() for char in s if char.isalnum())
        add_chars = ""
        for char in s:
            add_chars = char + add_chars
        # print(add_chars)    
        return s == add_chars
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("racecar"))  # Output: True
    print(sol.isPalindrome("hello"))     # Output: False
    print(sol.isPalindrome("A man, a plan, a canal: Panama")) # Output: False