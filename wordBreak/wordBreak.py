class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # empty string can be segmented

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]

if __name__ == "__main__":
    sol = Solution()
    result = sol.wordBreak("leetcode", ["leet", "code"])  # Output: True
    print(result)

    