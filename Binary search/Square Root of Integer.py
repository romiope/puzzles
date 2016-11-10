class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 1:
            return 1
        first = 0
        last = A

        while True:
            mid = int(((last - first) / 2) + first)
            x = mid ** 2
            if x == A or (x < A and ((mid + 1) ** 2) > A):
                return mid

            if x > A:
                last = mid
            elif x < A:
                first = mid

