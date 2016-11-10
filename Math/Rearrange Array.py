class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        m = [i for i in A]
        for i in xrange(len(A)):
            i_ = m[m[i]]
            A[i] = i_