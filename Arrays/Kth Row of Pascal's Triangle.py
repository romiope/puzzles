class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        return generate(A)


def generate(k=0):
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