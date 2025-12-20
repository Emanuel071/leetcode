# string_example = "applepenapple"
# word_list = ["apple", "pen"]

# length_string = len(string_example)

# length_word_list = len(word_list)

# flag = True

# for word in word_list:
#     # print(word)
#     if word not in string_example:
#         flag = False
#         break

# print(flag)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        flag = True
        temp_s = ""

        for word in wordDict:
            print(word)
            print(s)
            if word not in s:
                flag = False
                break


        while wordDict:
            temp_s += wordDict.pop()

        if len(s) < len(temp_s):
            flag = False
        

        
        return flag

if __name__ == "__main__":
    sol = Solution()
    result = sol.wordBreak("leetcode", ["leet","code"])  # Output: True
    print(result)