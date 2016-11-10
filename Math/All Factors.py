class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        if A is 1:
            return [1]
        from math import sqrt
        r = []
        a = int(sqrt(A))
        for i in xrange(1, a+1):
            if A % i == 0:
                r.append(i)
        m = []
        for i in r:
            if A % i == 0:
                a_i = A / i
                if a_i not in r:
                    m.append(a_i)
        r.extend(reversed(m))
        return r if len(r) > 0 else [1]