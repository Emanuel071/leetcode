class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Convert wordDict to a set for O(1) lookup time
        word_set = set(wordDict)
        # dp[i] represents whether s[0:i] can be segmented into words from wordDict
        dp = [False] * (len(s) + 1)
        # Base case: empty string can always be segmented
        dp[0] = True

        # Iterate through each position in the string
        for i in range(1, len(s) + 1):
            # Check all possible previous positions
            for j in range(i):
                # If s[0:j] is segmentable and s[j:i] exists in wordDict, mark s[0:i] as segmentable
                print(dp[j], s[j:i])
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further for this position

        # Return whether the entire string can be segmented
        return dp[len(s)]

if __name__ == "__main__":
    sol = Solution()
    result = sol.wordBreak("leetcode", ["leet", "code"])  # Output: True
    print(result)

