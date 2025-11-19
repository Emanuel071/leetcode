class Solution(object):        
    def climbStairs(n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1

        first = 1
        second = 1
        # print(range(2, n + 1))
        for _ in range(2, n + 1):
            third = first + second
            first = second
            second = third

        return second


if __name__ == "__main__":
    result = Solution.climbStairs(5)  # Output: 8
    print(result)