class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        first = 0
        last = len(A) - 1
        if A[0] > B or A[last] < B:
            return [-1, -1]

        while A[first] != B:
            if first == last:
                return [-1, -1]
            mid = int(((last - first) / 2) + first)
            if last - first == 1:
                if A[first] < B <= A[last]:
                    first = last
                else:
                    return [-1, -1]
            elif A[mid] < B:
                first = mid
            elif A[mid] >= B:
                last = mid

        tail = first
        last = len(A) - 1
        while A[last] != B:
            mid = int(((last - tail) / 2) + tail)
            if last - tail == 1:
                if A[tail] == B < A[last]:
                    last = tail
                else:
                    return [-1, -1]
            elif A[mid] > B:
                last = mid
            elif A[mid] == B:
                tail = mid

        return [first, last]