class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        ss = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
              50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        r = ''
        for i in sorted(ss.keys())[::-1]:
            d = A / i
            r += ss[i] * d
            A -= i * d
        return r
