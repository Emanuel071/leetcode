class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(5))  # Output: [0,1,1,2,1,2]
    print(sol.countBits(2))  # Output: [0,1,1]
    print(sol.countBits(0))  # Output: [0]
    