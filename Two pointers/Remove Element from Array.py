class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        p1 = 0
        p2 = 1
        while p2 < len(A):
            if A[p1] == B and A[p2] != B:
                A[p1] = A[p2]
                A[p2] = B
                p1 += 1
                p2 += 1
                continue
            if A[p1] != B:
                p1 += 1
            if A[p2] == B:
                p2 += 1
            if p2 <= p1:
                p2 = p1 + 1

        while p1 < len(A) and A[p1] != B:
            p1 += 1
        return p1