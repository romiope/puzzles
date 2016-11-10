class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i = 0
        k = 0
        l = len(A)
        l2 = len(B)
        r = []
        while i < l:
            if k == l2:
                break
            if A[i] > B[k]:
                k += 1
            elif A[i] == B[k]:
                r.append(B[k])
                k += 1
                i += 1
            elif A[i] < B[k]:
                i += 1
        return r