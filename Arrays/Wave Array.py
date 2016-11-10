class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        ln = len(A)
        A = sorted(A)
        c = 0
        while c < ln and c+1 < ln:
            val = A[c]
            A[c] = A[c+1]
            A[c+1] = val
            c += 2
        return A