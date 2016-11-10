class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if haystack == "" or needle == "" or len(needle) > len(haystack):
            return -1

        for i in xrange(len(haystack)):
            c = 0
            while c + i < len(haystack) and c < len(needle) and needle[c] == haystack[i + c]:
                c += 1
            if c == len(needle):
                return i
        return -1