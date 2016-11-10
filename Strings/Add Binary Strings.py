class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        return bin(long(A, base=2) + long(B, base=2)).split('b')[1]