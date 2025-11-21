class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        encoded = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            encoded.append(s[i] + str(count))
            i += 1
        return ''.join(encoded)
    def decode(self, s):
        """
        :type s: str
        :rtype: str
        """
        decoded = []
        i = 0
        while i < len(s):
            char = s[i]
            i += 1
            count_str = []
            while i < len(s) and s[i].isdigit():
                count_str.append(s[i])
                i += 1
            count = int(''.join(count_str))
            decoded.append(char * count)
        return ''.join(decoded)

if __name__ == "__main__":
    sol = Solution()
    original = "aaabbbccdaa"
    encoded = sol.encode(original)
    print("Encoded:", encoded)  # Output: "a3b3c2d1a2"
    decoded = sol.decode(encoded)
    print("Decoded:", decoded)  # Output: "aaabbbccdaa"
    print("Decoding matches original:", decoded == original)  # Output: True
    