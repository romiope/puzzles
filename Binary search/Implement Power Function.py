class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if n == 0:
            return 1 % d
        if x == 0:
            return 0

        base = x
        r = 1
        while n > 0:
            if n % 2 == 1:
                r = (r * base) % d
                n -= 1
            base = (base * base) % d
            n >>= 1
        return r % d