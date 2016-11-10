class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        if n == 0 or n == 1:
            return 0
        i = 0
        j = 1

        while i < n - 1 and j < n:
            if i != j and A[j] - A[i] == B:
                return 1

            if A[j] - A[i] < B:
                j += 1
            else:
                i += 1

        return 0