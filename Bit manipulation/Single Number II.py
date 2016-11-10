class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        d1 = dict()
        d2 = dict()
        for i in A:
            if d2.get(i, 0) == 0:
                if d1.get(i, 0) == 0:
                    d1[i] = 1
                else:
                    d2[i] = d1.pop(i)
        return d1.keys()[0]
