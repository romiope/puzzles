class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        m = 1
        f = 0
        while True:
            m *= 5
            i = int(A / m)
            if i == 0:
                break
            f += i

        return f