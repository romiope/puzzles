class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        g = bin(A).split('b')[1]
        while len(g) != 32:
            g = '0'+g
        g = g[::-1]
        return int(g, 2)