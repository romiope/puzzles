class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        if len(B) == 1 and B[0] == "0" or A[0] == "0" and len(A) == 1:
            return "0"

        stois = lambda s: map(int, s)
        istos = lambda a: "".join(map(str, a))

        if len(A) < len(B):
            m = A
            A = B
            B = m

        A = stois(A)
        B = stois(B)

        res = []
        for i, m in enumerate(B[::-1]):
            if m == 0:
                continue

            mem = 0
            r_m_mul = [] + [0] * i
            for item in A[::-1]:
                r = (item * m) + mem
                if r > 9:
                    r_m_mul += [r % 10]
                    mem = r / 10
                else:
                    r_m_mul += [r]
                    mem = 0
            if mem > 0:
                r_m_mul += [mem]
            res.append(r_m_mul)

        del A
        del B

        n = max(map(len, res))

        fres = []
        mem = 0
        for i in xrange(0, n):
            frow = sum([(j[i:i + 1] or [0])[0] for j in res]) + mem
            if frow > 9:
                fres += [frow % 10]
                mem = frow / 10
            else:
                fres += [frow]
                mem = 0
        if mem:
            fres += [mem]

        fres = fres[::-1]
        n = 0
        while n < len(fres) - 1:
            if fres[n] == 0:
                fres.remove(n)
            else:
                break

        return "".join(map(str, fres))