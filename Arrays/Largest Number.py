class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):

        def comparator(a, b):
            if int(str(a) + str(b)) == int(str(b) + str(a)):
                return 0
            if int(str(a) + str(b)) < int(str(b) + str(a)):
                return 1
            else:
                return -1

        r = str(int("".join(map(str, sorted(A, cmp=comparator)))))
        return r