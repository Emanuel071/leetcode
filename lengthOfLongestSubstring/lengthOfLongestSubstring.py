class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # print(char_index_map)
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1
                # print("Updated left:", left)
            char_index_map[char] = right
            max_length = max(max_length, right - left + 1)
            # print("Current max_length:", max_length)
            print("right:", right, " char:", char, " left:", left, " max_length:", max_length)
            print("Updated char_index_map:", char_index_map)
            print("----")
        
        return max_length
    
if __name__ == "__main__":
    sol = Solution()
    # print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    # print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3    