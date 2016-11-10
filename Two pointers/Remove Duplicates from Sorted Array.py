class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        r = 1

        for i in xrange(1, len(A)):
            if A[i] != A[i - 1]:
                A[r] = A[i]
                r += 1

        return r