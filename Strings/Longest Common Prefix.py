class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if not A:
            return ""

        value = list(sorted(A, key=lambda a: len(a)))[0]

        for item in A:
            new_value = ""
            i = 0
            while len(value) > i and item[i] == value[i]:
                new_value += value[i]
                i += 1
            value = new_value
        return value
