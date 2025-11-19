class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Given two integers a and b, return the sum of the two integers without using the operators + and -.
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
            # print(f"Intermediate Sum: {a}, Carry: {b}")  # Debug statement
        return a    
if __name__ == "__main__":
    sol = Solution()
    print(sol.getSum(1, 2))  # Output: 3
    print(sol.getSum(2, 3))  # Output: 5