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
    # result = sol.wordBreak("leetcode", ["leet","code"])  # Output: True
    # print(result)

s = "leetcode"
# Iterate through each position in the string
for i in range(1, len(s) + 1):
    # print("index: ", i)
    # print("s[0:i]: ", s[0:i])
    # Check all possible previous positions
    for j in range(i):
        print("  j index: ", j)
        print("  s[0:j]: ", s[0:j])
        print("  s[j:i]: ", s[j:i])
        print("----")   


