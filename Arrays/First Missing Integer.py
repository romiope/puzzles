class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):

        l = len(A)
        for i, item in enumerate(A):
            if 1 > item or item > l:
                A[i] = l + 1

        for i in A:
            if abs(i) != l + 1:
                A[abs(i) - 1] *= -1

        for i, item in enumerate(A):
            if item > 0:
                return i + 1
        return l + 1