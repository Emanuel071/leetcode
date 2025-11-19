class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Given two integers a and b, return the sum of the two integers without using the operators + and -.
        # faster version using binary operations
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a