class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        res = ""
        while True:
            A, m = divmod(A-1, 26)
            res = chr(m+ ord('A')) + res
            if not A: return res
        return res