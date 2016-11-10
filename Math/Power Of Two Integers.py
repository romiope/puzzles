class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        if A == 0:
            return False
        if A == 1:
            return True
        for i in xrange(2, 33):
            for m in xrange(2, (int(A ** (1.0/i))+2)):
                if m ** i == A:
                    return True
        return False