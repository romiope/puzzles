class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        r = [0 for i in range(max(A)+1)]
        for i in A:
            r[i] += 1
        return r.index(max(r))