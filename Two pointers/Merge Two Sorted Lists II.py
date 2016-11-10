class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        n = 0
        while n < len(A) and B:
            if A[n] > B[0]:
                A.insert(n, B[0])
                del B[0]
            else:
                n += 1

        return A + B