class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary representation: 1011
        # number of '1's: 3
        count = 0
        while n:
            print(f"n before: {bin(n)}, count: {count}")
            count += n & 1
            print(f"n & 1: {n & 1}")
            n >>= 1
            print(f"n after: {bin(n)}, count: {count}\n")
        return count

if __name__ == "__main__":
    sol = Solution()
    count = sol.hammingWeight(11)  # Output: 3
    
