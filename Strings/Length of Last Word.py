class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        r = 0
        n = len(A) - 1
        while n >= 0:
            if A[n] == ' ':
                if r > 0:
                    return r
            else:
                r += 1
            n -= 1
        return r