class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        count = {}
        max_count = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            print((right - left + 1))
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            print("left:", left, " right:", right, " max_count:", max_count, "max_length:", max_length)
            print("count dict:", count)
            print("---")
        # print(count)
        return max_length

if __name__ == "__main__":
    sol = Solution()
    # print(sol.characterReplacement("AABABBA", 1))  
    print(sol.characterReplacement("ABAB", 2))  
    # print(sol.characterReplacement("AABABBA", 2))
    # print(sol.characterReplacement("AAAA", 2))
    # print(sol.characterReplacement("ABCDE", 1)) #output: 2
