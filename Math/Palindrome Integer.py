class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        if A < 0:
            return 0
        s = str(A)
        k = len(s) - 1
        for i in xrange((len(s)/2) + 1):
            if s[i] != s[k - i]:
                return 0
        return 1