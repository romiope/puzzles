class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        g = 0
        for i in A:
            g = g ^ i
        return g