import sys
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        negative = A < 0
        r = int(str(abs(A))[::-1])
        r = -r if negative else r
        return 0 if r > 2**31 or r < -2**31 else r