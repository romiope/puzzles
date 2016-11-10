class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        r = []
        maximum = (1 << 31) - 1
        minimum = -(1 << 31)

        numbers = "0123456789"
        symbols = "-+"

        for i in A:
            if not r and i != " " and i not in symbols and i not in numbers:
                return 0
            if not r and i == " ":
                continue
            if r and i not in numbers:
                break
            if not r and i in symbols or i in numbers:
                r.append(i)
                continue
            if r and len(r) == 1 and i not in symbols and i not in numbers:
                return 0

        if not r:
            return 0

        try:
            r = int("".join(r))
            if r > maximum:
                return maximum
            if r < minimum:
                return minimum
            return r
        except:
            return 0


