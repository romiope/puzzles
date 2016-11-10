class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B == 1:
            return A
        rize = True

        r = [[] for i in xrange(0, B)]

        p = 0
        for i in A:
            r[p].append(i)
            if rize:
                p += 1
            else:
                p -= 1
            if p == B - 1:
                rize = False
            if p == 0:
                rize = True

        r = reduce(lambda a, b: a + b, r)
        return "".join(map(str, map(str, r)))