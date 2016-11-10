class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        if not A:
            return -1
        if len(A) == 1:
            if A[0] == b:
                return 0
            else:
                return -1

        first = 0
        last = len(A) - 1

        while True:
            mid = (last - first) / 2 + first
            if A[mid] == B:
                return mid
            if A[first] == B:
                return first
            if A[last] == B:
                return last
            if first == last or last - first == 1:
                return -1

            if A[mid] < A[last]:
                if A[mid] < B < A[last]:
                    first = mid
                else:
                    last = mid

            if A[first] < A[mid]:
                if A[first] < B < A[mid]:
                    last = mid
                else:
                    first = mid

        return -1