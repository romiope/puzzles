class Solution:
    # @param A : string
    # @return an integer

    # Number	4	9	40	90	400	900
    # Notation	IV	IX	XL	XC	CD	CM

    # Symbol	I	V	X	L	C	D	M
    # Value	1	5	10	50	100	500	1,000

    def romanToInt(self, A):

        s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sm = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        r = 0
        p = len(A) - 1
        while p >= 0:
            jjj = sm.get(A[p-1] + A[p], 0)
            if p > 0 and jjj > 0:
                p -= 1
                r += jjj
            else:
                r += s.get(A[p], 0)
            p -= 1

        return r