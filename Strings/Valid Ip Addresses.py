class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        def take_first(a):
            return [[int(a[:i]), a[i:]] for i in xrange(1, 4) if int(a[:i]) <= 255 and a[:i] not in ["00", "000"]]

        def calc_variants(source, result, acc=()):
            if len(acc) > 4:
                return
            if not source:
                if len(acc) == 4 and len(reduce(lambda a, b: a + b, map(str, acc))) == len(A):
                    result.append(".".join(map(str, acc)))
                return
            for i, j in take_first(source):
                calc_variants(j, l, acc + (i,))

        l = []
        calc_variants(A, l)

        l = list(set(l))
        def cm(a, b):
            to_ints = lambda x: map(int, x.split('.'))
            a = to_ints(a)
            b = to_ints(b)
            for i, item in enumerate(a):
                if item == b[i]:
                    continue
                return item - b[i]
            return 0
        return sorted(l, cmp=cm)