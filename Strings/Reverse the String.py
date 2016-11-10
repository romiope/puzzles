class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        return " ".join(filter(lambda x: len(x) > 0, A.split(' '))[::-1])