class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A == 1 or B == 1:
            return 1
        row = k_row(A + B - 2)
        return row[min(A, B) - 1]


def k_row(k=0):
    line = [1]
    for i in xrange(k):
        line = list(grow(line))
    return line


def grow(l):
    size = len(l) + 1
    for i in xrange(1, size + 1):
        if i is 1 or i is size:
            yield 1
        else:
            yield l[i - 1] + l[i - 2]