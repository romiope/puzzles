class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        g = bin(A)
        r = 0
        for i in list(g):
            if i == '1':
                r += 1
        return r