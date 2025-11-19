class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        listofints = [a,b]

        # print(sum(listofints))
        return sum(listofints)

if __name__ == "__main__":
    sol = Solution()
    print(sol.getSum(1, 2))  # Output: 3
    print(sol.getSum(2, 3))  # Output: 0
