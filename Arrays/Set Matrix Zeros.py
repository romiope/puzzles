class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])
        r = []
        col = []

        for row in A:
            r.append([0] * n if 0 in row else [1] * n)
            for j, pos in enumerate(row):
                if not pos and j not in col:
                    col.append(j)

        for i in xrange(m):
            for j in col:
                r[i][j] = 0
        return r