class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):

        a = 0
        b = 0

        l = [1 for i in xrange(0, len(A))]
        for i in A:
            ind = i - 1
            if l[ind] > 0:
                l[ind] *= (-1)
            else:
                a = i

        for i, it in enumerate(l):
            if it > 0:
                b = i + 1

        return [a, b]