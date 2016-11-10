class Solution:
    # @param A : integer
    # @return a list of integers
    def generate(self, A):
        if A is 0:
            return []
        return list(self.g(A - 1))

    def grow(self, l):
        size = len(l) + 1
        for i in xrange(1, size + 1):
            yield 1 if i is 1 or i is size else l[i - 1] + l[i - 2]

    def g(self, k=0):
        line = [1]
        yield line
        for i in xrange(k):
            line = list(self.grow(line))
            yield line