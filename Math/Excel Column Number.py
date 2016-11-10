class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        import string
        u = string.ascii_uppercase

        def val(c):
            return u.find(c) + 1

        v = 0
        p = 0
        for i in reversed(A):
            v += val(i) * 26 ** p
            p += 1
        return v