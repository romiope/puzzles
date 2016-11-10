class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A = self.remove_zeros_from_end(A[::-1]) + [0]
        p = 1
        for i, item in enumerate(A):
            item_p = item + p
            A[i] = item_p if item_p <= 9 else item_p - 10
            if item_p > 9:
                p = item_p - 9
            else:
                break

        A = A[::-1]
        return A if A[0] is not 0 else A[1::]

    def remove_zeros_from_end(self, l):
        p = len(l)
        for i in xrange(p - 1, -1, -1):
            if l[i] is 0:
                l.pop()
            else:
                return l
        return l