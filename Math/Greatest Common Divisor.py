class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A == 0:
            return B
        elif B == 0:
            return A

        m = A if A < B else B

        while m > 1:
            if B % m == 0 and A % m == 0:
                break
            m -= 1

        return m