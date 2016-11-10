class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        ha = len(A)
        wa = len(A[0])

        r = [[0 for i in range(ha)] for x in range(wa)]

        for n, line in enumerate(A):
            for p, item in enumerate(line):
                r[p][ha - n - 1] = item
        return r